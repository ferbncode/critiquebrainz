from critiquebrainz import db
from critiquebrainz.db import exceptions as db_exceptions
import sqlalchemy
from collections import OrderedDict

# function names need a lot to change

def get(review_id, order_desc=False):
    """Get revisions on a review optionally ordered by the timestamp"""
    with db.engine.connect() as connection:
        if (order_desc == True):
            result = connection.execute(sqlalchemy.text("""
                SELECT id, text, timestamp
                 FROM revision
                WHERE review_id = :review_id
                 ORDER BY timestamp DESC;
            """), {
                "review_id": review_id,
            })
        else:
            result = connection.execute(sqlalchemy.text("""
                SELECT id, timestamp, text
                 FROM revision
                WHERE review_id = :review_id
            """), {
                "review_id": review_id,
            })

        rows = result.fetchall()
        count = len(rows)
    return rows, count

def get_votes(review_id):
    """Get vote count for the respective revisions optionally ordered by the timestamp"""

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT DISTINCT revision.id, user_id, vote, timestamp
             FROM revision LEFT JOIN vote
            ON vote.revision_id = revision.id
             WHERE review_id = :review_id
            ORDER BY timestamp DESC;
        """),{
            "review_id": review_id,
            })
        rows = result.fetchall()
        votes = OrderedDict()
        for row in rows:
            revision = row.id
            if(not votes.get(revision)):
                votes[revision] = {'positive':0, 'negative':0}
            if(row.vote == False):
                votes[revision]['negative'] += 1
            elif(row.vote == True):
                votes[revision]['positive'] += 1
    return votes
