import toml
import time
import logging
import logging.config
import socket
import select

from toml import TomlDecodeError

from chat_server import config
from chat_server.dao import insert_batch, insert_one, read_one, update_one

logger = logging.getLogger(__name__)


def setup():
    """
    Set up configuration and logging
    """

    from chat_server.logger import LOGGING

    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO
    )

    logging.config.dictConfig(LOGGING)

    return


def load_config(config_file):
    '''
    Read config file or read file
    '''

    config.CONFIG_FILE = config_file

    try:
        with open(config.CONFIG_FILE) as f:
            config.CHAT_CONFIG = toml.load(f)
            config.DATABASES['default'] = config.CHAT_CONFIG['postgres']
    except FileNotFoundError as e:
        raise Exception(f"config file {config.CONFIG_FILE} not found.")
    except TomlDecodeError as e:
        raise Exception(f"{config.CONFIG_FILE} is not a valid toml file")
    except Exception as e:
        raise e
    

def create_socket_server():
    """
        create server
    """
    server = None

    return server

def receive_message(client_socket):
    HEADER_LENGTH = 10
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False
    

def server_client_connection():

    IP = "127.0.0.1"
    PORT = 1234
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    sockets_list = [server_socket]
    clients = {}
    print(f'Listening for connections on IP = {IP} at PORT = {PORT}')

    while True:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()

                user = receive_message(client_socket)

                if user is False:
                    continue

                sockets_list.append(client_socket)
                clients[client_socket] = user

                print('Accepted new connection from {}:{}, username: {}'.format(
                    *client_address, user['data'].decode('utf-8')))
            else:
                message = receive_message(notified_socket)

                if message is False:
                    print('Closed connection from: {}'.format(
                        clients[notified_socket]['data'].decode('utf-8')))

                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]

                    continue

                user = clients[notified_socket]
                print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')


                if message["data"].decode("utf-8").lower() == "quit":
                    print("Server shutting down...")
                    for client_socket in sockets_list:
                        if client_socket != server_socket:
                            client_socket.close()
                    server_socket.close()
                    exit()

                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])



def broacast_message_to_all():
    """
    send the new messages to everyone
    """


def start_server():
    logging.info("Starting Chat Server")
    
    server_client_connection()

    # server = create_socket_server()

    # insert_batch()
    # read_one()
    update_one()

    # while True:  
    #     logger.info("waiting for connection")

    #     logger.info("connection made, recv msg")
    #     broacast_message_to_all()
    #     insert_batch()


    return