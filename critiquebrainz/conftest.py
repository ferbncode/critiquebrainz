import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from critiquebrainz.frontend.external.musicbrainz_db.utils import populate_db, remove_test_data
import critiquebrainz.frontend.external.musicbrainz_db as mb


TEST_DB_URI = 'postgres://musicbrainz:musicbrainz@musicbrainz_test_db:5432/musicbrainz_test'


@pytest.fixture(scope="session", autouse=True)
def populate_mb_database(request):
    mb.engine = create_engine(TEST_DB_URI, poolclass=NullPool)
    populate_db()
    def empty_mb_database():
        remove_test_data()
    request.addfinalizer(empty_mb_database)
