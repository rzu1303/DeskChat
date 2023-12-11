import sys

import logging
import argparse

from chat_server.services import (
    load_config, 
    setup, 
    start_server
)
from chat_server.db import chat_server_init_db
from chat_server import config

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Start Chat Server')

    parser.add_argument('-c', nargs=1, help='Yaml configuration file')

    args = parser.parse_args()

    config_file = args.c[0] if args.c is not None and len(
        args.c) > 0 else 'config.toml'
    
    load_config(config_file)
    setup()
    chat_server_init_db()

    logger.info("Starting Chat Server version %s" % config.PROJECT_VERSION)

    try:
        start_server()
    except:
        logging.exception('')
        sys.exit(1)


if __name__ == "__main__":
    main()