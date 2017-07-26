import os
import critiquebrainz.frontend.external.musicbrainz_db as mb

ADMIN_SQL_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..', 'admin', 'sql')

def populate_db():
    """Populate test database with the test data."""
    mb.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'create_test_data.sql'))

def remove_test_data():
    """Remove test data from the test database."""
    mb.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'delete_test_data.sql'))
