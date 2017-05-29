from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

MB_SCHEMA_VERSION = 1

engine = None

def init_db_engine(connect_str):
    global engine
    engine = create_engine(connect_str, poolclass=NullPool)
