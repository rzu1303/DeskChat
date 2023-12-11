'''this file should only have methods that builds connection to db'''
import logging
from sqlalchemy import create_engine

from chat_server.models.create import INIT_DB_QUERY
from chat_server import config

logger = logging.getLogger(__name__)


def _init_db(con):
    """
    Ensure the table exists on the database.
    """
    con.execute(INIT_DB_QUERY)


def chat_server_init_db():
    logger.info("Initializing database...")
    
    ENGINE = chat_server_create_engine()

    with ENGINE.connect() as con:
        _init_db(con)

    logger.info("Database initialization complete!")


def chat_server_create_engine():
    db_config = config.DATABASES['default']
    db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    
    ENGINE = create_engine(
        db_url,
        pool_size=30, max_overflow=0
    )

    return ENGINE
