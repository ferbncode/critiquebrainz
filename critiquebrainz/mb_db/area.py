from critiquebrainz import mb_db
import sys
import sqlalchemy

def get_all():
    with mb_db.mb_engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT name FROM area
        """))
        rows = result.fetchall()
    print (rows[:3], file=sys.stderr)
    return None

