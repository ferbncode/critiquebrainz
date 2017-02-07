from critiquebrainz import db
from critiquebrainz.db import exceptions as db_exceptions
import sqlalchemy
from critiquebrainz.data.model.mixins import DeleteMixin, AdminMixin


class User(AdminMixin, DeleteMixin):

    def __init__(self, user):
        self.id = user.get('id')
        self.display_name = user.get('display_name')
        self.email = user.get('email')
        self.created = user.get('created')
        self.musicbrainz_id = user.get('musicbrainz_id')
        self.show_gravatar = user.get('show_gravatar')
        self.is_blocked = user.get('is_blocked')


    @classmethod
    def get_by_id(cls, user_id):

        with db.engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("""
                SELECT *
                  FROM "user"
                 WHERE id = :user_id
            """), {
                "user_id": user_id
            })
            row = result.fetchone()
        return cls(dict(row)) if row else None


    @classmethod
    def create(cls, display_name, **kwargs):
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
        return cls(dict(user))


    @classmethod
    def get_by_mbid(cls, musicbrainz_id):
        with db.engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("""
                SELECT *
                FROM "user"
                WHERE musicbrainz_id = :musicbrainz_id
            """), {
                "musicbrainz_id": musicbrainz_id
            })
            row = result.fetchone()
        return cls(dict(row)) if row else None


