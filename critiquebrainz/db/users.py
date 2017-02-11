from hashlib import md5
from critiquebrainz.db import exceptions as db_exceptions
import critiquebrainz.db.revision as db_revision
import sqlalchemy
from critiquebrainz import db
from datetime import datetime
import uuid



def gravatar_url(source, default="identicon", rating="pg"):
    """Generates Gravatar URL from a source ID.

    Source string is hashed using the MD5 algorithm and included into a
    resulting URL. User's privacy should be considered when using this. For
    example, if using an email address, make sure that user explicitly allowed
    that.

    See https://en.gravatar.com/site/implement/images/ for implementation
    details.

    Args:
        source (str): String to be hashed and used as an avatar ID with the
            Gravatar service. Can be email, MusicBrainz username, or any other
            unique identifier.
        default (str): Default image to use if image for specified source is
            not found. Can be one of defaults provided by Gravatar (referenced
            by a keyword) or a publicly available image (as a full URL).
        rating (string): One of predefined audience rating values. Current
            default is recommended.

    Returns:
        URL to the Gravatar image.
    """
    return "https://gravatar.com/avatar/{hash}?d={default}&r={rating}".format(
        hash=md5(source.encode('utf-8')).hexdigest(),
        default=default,
        rating=rating,
    )


def get_many_by_mb_username(usernames):
    """Get information about users.

    Args:
        usernames (list): A list of MusicBrainz usernames. This lookup is case-insensetive.

    Returns:
        All columns of 'user' table (list of dictionaries)
        and avatar_url (Gravatar url).
        If the 'usernames' variable is an empty list function returns it back.
    """
    if not usernames:
        return []

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT id,
                   display_name,
                   email,
                   created,
                   musicbrainz_id,
                   show_gravatar
              FROM "user"
             WHERE musicbrainz_id ILIKE ANY(:musicbrainz_usernames)
        """), {
            'musicbrainz_usernames': usernames,
        })
        row = result.fetchall()
        users = [dict(r) for r in row]
        for user in users:
            default_gravatar_src = "%s@cb" % user["id"]
            if user["show_gravatar"]:
                user["avatar_url"] = gravatar_url(user.get("email") or default_gravatar_src)
            else:
                user["avatar_url"] = gravatar_url(default_gravatar_src)
        return users


def get_by_id(user_id):

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT *
              FROM "user"
             WHERE id = :user_id
        """), {
            "user_id": user_id
        })
        row = result.fetchone()
    return dict(row) if row else None


def create(display_name, **kwargs):
    id = str(uuid.uuid4())
    musicbrainz_id = kwargs.pop('musicbrainz_id', None)
    email = kwargs.pop('email', None)
    show_gravatar = kwargs.pop('show_gravatar', False)
    is_blocked = kwargs.pop('is_blocked', False)
    if(kwargs):
        raise TypeError('Unexpected **kwargs: %r' % kwargs)

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            INSERT INTO "user"
                 VALUES (:id, :display_name, :email, :created, :musicbrainz_id, :show_gravatar, :is_blocked)
              RETURNING id
            """), {
                "id": id,
                "display_name": display_name,
                "email": email,
                "created": datetime.now(),
                "musicbrainz_id": musicbrainz_id,
                "show_gravatar": show_gravatar,
                "is_blocked": is_blocked
            })
        new_id = result.fetchone()[0]
        user = get_user(new_id)
    return user


def get_by_mbid(musicbrainz_id):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT *
            FROM "user"
            WHERE musicbrainz_id = :musicbrainz_id
        """), {
            "musicbrainz_id": musicbrainz_id
        })
        row = result.fetchone()
    return dict(row) if row else None


def get_or_create(display_name, musicbrainz_id, **kwargs):

    user = get_by_mbid(musicbrainz_id)
    if not user:
        user = create(display_name, musicbrainz_id=musicbrainz_id, **kwargs)
    return user


def get_count():

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT count(*)
              FROM "user"
        """))
        count = result.fetchone()[0]
    return count


def list(limit=0, offset=0):

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT *
              FROM "user"
             LIMIT :limit
            OFFSET :offset
        """), {
            "limit": limit,
            "offset": offset
        })
        rows = result.fetchall()
        if not rows:
            raise db_exceptions.NoDataFoundException("No users found")
        else:
            rows = [dict(row) for row in rows]
    return rows


def unblock(user_id):

    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            UPDATE "user"
               SET is_blocked = 'false'
             WHERE id = :user_id
        """), {
            "user_id": user_id
        })


def block(user_id):

    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            UPDATE "user"
               SET is_blocked = 'true'
            WHERE id = :user_id
        """), {
            "user_id": user_id
        })


def has_voted(user_id, review_id):

    last_revision = db_revision.get(review_id, limit=1)[0]
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT count(*)
              FROM vote
             WHERE revision_id = :revision_id
               AND user_id = :user_id
            """), {
                "revision_id": last_revision['id'],
                "user_id": user_id
            })
        count = result.fetchone()[0]
        return count > 0


def karma(user_id):

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT user_id, vote
              FROM ((vote
         LEFT JOIN revision
                ON revision.id = revision_id)
         LEFT JOIN review
                ON review.id = review_id)
         LEFT JOIN "user"
                ON "user".id = review.user_id
             WHERE "user".id = :user_id
        """), {
            "user_id": user_id
        })

        rows = result.fetchall()
        _karma = 0
        for row in rows:
            if row.vote == 't':
                _karma += 1
            else:
                _karma -= 1
    return _karma


def reviews(user_id):

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT *
              FROM review
             WHERE user_id = :user_id
        """), {
            "user_id": user_id
        })

        rows = result.fetchall()
        rows = [dict(row) for row in rows]

    return rows


def get_votes(user_id, date='1-1-1970'):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT vote
              FROM vote
             WHERE user_id = :user_id
               AND rated_at >= :date
        """), {
            "user_id": user_id,
            "date": date
        })

        rows = result.fetchall()
        rows = [dict(row) for row in rows]

    return rows


def get_reviews(user_id, date='1-1-1970'):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
           SELECT *
           FROM review
      LEFT JOIN
        (SELECT review_id,
                min(timestamp)
             AS creation_time
           FROM revision
       GROUP BY review_id)
             AS review_create
             ON review.id = review_id
          WHERE user = :user_id
            AND creation_time > date
        """), {
            "user_id": user_id,
            "date": date
        })

        rows = result.fetchall()
        rows = [dict(row) for row in rows]

    return rows


def update(user, dispaly_name=None, email=None, show_gravatar=None):
    if display_name is None:
        display_name = user.display_name
    if show_gravatar is None:
        show_gravatar = user.show_gravatar
    if email is None:
        email = user.email

    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            UPDATE "user"
               SET display_name = display_name,
                  show_gravatar = show_gravatar,
                           email = email
             WHERE user_id = :user_id
        """), {
            "user_id": user.id,
        })
