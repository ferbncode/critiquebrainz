from critiquebrainz import mb_db
# from mb_db import db_exceptions
import sys
import sqlalchemy
from brainzutils import cache
from critiquebrainz.mb_db import db_helpers


## This is just an example function:
def search_artists(query_string):
    """Search for an artist on CritiqueBrainz"""

    with mb_db.mb_engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT artist_entity.id,
                   artist_entity.sort_name,
                   artist_entity.type,
                   artist_entity.gender,
                   artist_entity.area,
                   MAX(rank) AS rank
              FROM (
                SELECT name, ts_rank_cd(to_tsvector('mb_simple', name), query) AS rank
                FROM
                  (
                    SELECT name FROM artist
                    UNION ALL
                    SELECT sort_name AS name FROM artist
                  ) artist_names,
               plainto_tsquery('mb_simple', :query_string) AS query
               WHERE to_tsvector('mb_simple', name) @@ query OR name = :query_string
               ORDER  BY rank DESC
               ) AS r
          LEFT JOIN artist as artist_entity ON (artist_entity.name = r.name OR artist_entity.sort_name = r.name)
          GROUP BY artist_entity.gid, artist_entity.id
          ORDER BY rank DESC
        """),{
            "query_string": query_string
        })
        rows = result.fetchall()
        print(rows)
        rows = [dict(row) for row in rows]
    return rows
