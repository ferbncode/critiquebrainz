from sqlalchemy import create_engine
from critiquebrainz.frontend import create_app
from flask_testing import TestCase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
import os
import mbdata.config

TEST_DATABASE = "postgresql://musicbrainz:musicbrainz@musicbrainz_test_db/musicbrainz_db"

engine = create_engine(TEST_DATABASE)
mbdata.config.configure()

from mbdata import models
from mbdata.sample_data import create_sample_data

class MBDatabaseTestCase(TestCase):

    def create_app(self):
        app = create_app(config_path=os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '../../..', 'test_config.py'
        ))
        return app

    def setUp(self):
        # self.tearDown()
        conn = engine.connect()
        conn.execute("CREATE extension if not exists cube")
        engine.execute(CreateSchema('musicbrainz'))
        engine.execute(CreateSchema('cover_art_archive'))
        engine.execute(CreateSchema('wikidocs'))
        engine.execute(CreateSchema('documentation'))
        engine.execute(CreateSchema('statistics'))
        Session = sessionmaker(bind=engine)
        models.Base.metadata.create_all(engine)
        session = Session()
        create_sample_data(session)


    def tearDown(self):
        conn = engine.connect()
        conn.execute("DROP schema musicbrainz cascade")
        conn.execute("DROP schema cover_art_archive cascade")
        conn.execute("DROP schema wikidocs cascade")
        conn.execute("DROP schema documentation cascade")
        conn.execute("DROP schema statistics cascade")
        conn.close()
