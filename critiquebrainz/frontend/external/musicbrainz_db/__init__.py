from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from contextlib import contextmanager

engine = None

def init_db_engine(connect_str):
    global engine, Session
    engine = create_engine(connect_str, poolclass=NullPool)
    Session = scoped_session(
        sessionmaker(bind=engine)
    )

@contextmanager
def mb_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
