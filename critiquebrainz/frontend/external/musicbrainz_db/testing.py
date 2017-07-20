import os
from flask_testing import TestCase
from critiquebrainz.frontend import create_app
from critiquebrainz.frontend.external.musicbrainz_db import mb_session
from critiquebrainz.frontend.external.musicbrainz_db.utils import create_all, drop_all
from critiquebrainz.frontend.external.musicbrainz_db.sample_data import create_sample_data


class MBDatabaseTestCase(TestCase):

    def create_app(self):
        app = create_app(config_path=os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '../../..', 'test_config.py'
        ))
        return app

    def setUp(self):
        create_all()
        with mb_session() as session:
            create_sample_data(session)

    def tearDown(self):
        drop_all()
