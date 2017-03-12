from critiquebrainz import mb_db
# from mb_db import db_exceptions
import sys
import sqlalchemy
from brainzutils import cache



def get_tags(id, entity_type, relation, colname):

    ## Example function for get_tags. Many entities may
    ## require tags.
    query = """SELECT tag.name
                 FROM {}
           INNER JOIN tag
                   ON {}.tag = tag.id
           INNER JOIN {}
                   ON {}.id = {}.{}
                WHERE {}.gid = :id
            """.format(relation, relation, entity_type,
                    entity_type, relation, colname, entity_type)
    query = sqlalchemy.text(query)

    with mb_db.mb_engine.connect() as connection:
        results = connection.execute(query, {"id": id})
        tags = results.fetchall()
    tags_all = []
    if tags:
        for tag in tags:
            tags_all.append(str(tag[0]))
    return tags_all








