from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLAlchemyConfig, MYSQLConfig
from server.models.base import Base

engine = create_engine(
    MYSQLConfig.MYSQLDB_URL,
    pool_recycle=SQLAlchemyConfig.SQLALCHEMY_POOL_RECYCLE,
    pool_timeout=SQLAlchemyConfig.SQLALCHEMY_POOL_TIMEOUT,
    pool_size=SQLAlchemyConfig.SQLALCHEMY_POOL_SIZE,
    max_overflow=SQLAlchemyConfig.SQLALCHEMY_MAX_OVERFLOW
)

Session = sessionmaker(bind=engine)


@contextmanager
def get_db_session():
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
