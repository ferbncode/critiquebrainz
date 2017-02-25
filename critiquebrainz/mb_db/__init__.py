from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

SCHEMA_VERSION = 1
mb_engine = None

def init_db_engine(connect_str):
    global mb_engine
    mb_engine = create_engine(connect_str, poolclass=NullPool)

