from critiquebrainz import mb_db
from mb_db import db_exceptions
import sys
import sqlalchemy
from brainzutils import cache
from critiquebrainz.mb_db import db_helpers

# example function to get tags, release_group, artists, url_rels
def get_release_group_by_id(id, relations=[]):
    """(Example function)Get release group with the MusicBrainz ID."""

    key = cache.gen_key(id)
    release_group = cache.get(key)

    if not release_group:
        with mb_db.mb_engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("""
                SELECT r.id,
                       r.name,
                       artist_credit,
                       ty.name AS type
                  FROM release_group AS rg
             LEFT JOIN release_group_primary_type AS ty
                    ON type = ty.id;
                 WHERE r.gid = :release_group_id
            """),{
                "release_group_id": id,
            })
        row = result.fetchone()
        release_group = dict(row)
        if not rows:
            raise NoDataFoundError("No data Found")

    if "artists" in relations:
        # Use artist credit. l_artist_release_group does not have
        # all mappings.
        with mb_db.mb_engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("""
                SELECT artist.name,
                       artist.gid as id,
                  FROM artist
                  JOIN release_group
                    ON artist_credit = artist.id
                 WHERE release_group.gid = :release_group_id
            """), {
                "release_group_id": id,
            })
            artist = result.fetchone()[0]
            if artist:
                release_group["artist"] = artist;

    if "url-rels" in relations:
        with mb_db.db_engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("""
            SELECT url.id,
                   url.gid,
                   url.url,
                   link_type.name,
                   release_group.gid,
                   release_group.name
              FROM l_release_group_url
        INNER JOIN url
                ON url.id = l_release_group_url.entity1
        INNER JOIN release_group
                ON l_release_group_url.entity1 = release_group.id
        INNER JOIN link
                ON l_release_group_url.link = link.id
        INNER JOIN link_type
           ON link.link_type=link_type.id
        WHERE release_group.gid = :id
        """), {
            "id": id,
        })
        url_relations = result.fetchall()
        # Urls can be arranged then in a dictionary as critiquebrainz.frontend.external.relationships does
        if url_relations:
            release_group["url-relations"] = url_relations

    ## Adding new features can be easier in this case.
    ## Eg. Adding tags,

    if "tags" in relations:

        ## We can use helpers for things common between entities.
        ## This is similar to what Search Server actually does.
        tags = db_helpers.get_tags(id, 'release_group', 'release_group_tag', 'release_group')
        if tags:
            release_group["tags"] = tags

    ## Cache results as it is done presently
    cache.set(key=key, val=release_group, time=DEFAUTL_CACHE_EXPIRATION)
