"""
This module defines pytest fixtures and hooks which are used for configuring the test environment.
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from critiquebrainz.frontend.external.musicbrainz_db.utils import populate_db, remove_test_data
import critiquebrainz.frontend.external.musicbrainz_db as mb


TEST_DB_URI = 'postgres://musicbrainz:musicbrainz@musicbrainz_test_db:5432/musicbrainz_test'


@pytest.fixture(scope="session", autouse=True)
def populate_mb_database(request):
    """Populate MusicBrainz test db with the test data at start of a test session
    and remove the added test data after the test session completes."""
    mb.engine = create_engine(TEST_DB_URI, poolclass=NullPool)
    populate_db()
    def empty_mb_database():
        remove_test_data()
    request.addfinalizer(empty_mb_database)


def pytest_keyboard_interrupt(excinfo):
    #pylint: disable=unused-argument
    """Remove test data from the test db in case of a keyboard interrupt."""
    remove_test_data()
