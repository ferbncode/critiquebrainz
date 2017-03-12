from critiquebrainz import mb_db
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
                SELECT rg.id,
                       rg.name,
                       rg.artist_credit,
                       ty.name AS type
                       artist.name,
                       artist.gid as artist_id
                  FROM release_group AS rg
                  JOIN release_group_primary_type AS ty
                    ON rg.type = ty.id
                  JOIN artist
                    ON rg.artist_credit = artist.id
                 WHERE rg.gid = :release_group_id
            """),{
                "release_group_id": id,
            })
        row = result.fetchone()
        release_group = dict(row)
        # The data fetched needs to be properly arranged
        # in dictionaries.
        if not rows:
            raise NoDataFoundError("No data Found")


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
    cache.set(key=key, val=release_group, time=DEFAULT_CACHE_EXPIRATION)
