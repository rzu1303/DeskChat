import os
import queue

from chat_server import version

PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_VERSION = version.__version__

DATABASES = {

    'default': {
        "user": os.getenv('DEFAULT_DB_USER', 'postgres'),
        "password":  os.getenv('DEFAULT_DB_PASS', ''),
        "host":  os.getenv('DEFAULT_DB_HOST', 'localhost'),
        "port": int(os.getenv('DEFAULT_DB_PORT', '5432')),
        "dbname": os.getenv('DEFAULT_DB_NAME', 'postgres'),
    }

}

CONFIG_FILE = None
CHAT_CONFIG = None
AGENT_CONFIG = None

# socket network 
IP = "127.0.0.1"
PORT = 1234
HEADER_LENGTH = 10
