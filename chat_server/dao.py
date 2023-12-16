'''all type of database operation'''
from chat_server.db import chat_server_create_engine
from chat_server.models.chat_server_autogen import ChatServerMessage
from sqlalchemy.orm import sessionmaker
from chat_server import config
import logging

def insert_one():
    """
    insert one message
    """
    ENGINE = chat_server_create_engine()

    if  not config.TABLE_DATA.empty():
        logging.info("insert_one function")
        temporary_data = config.TABLE_DATA.get()
        temporary_name = temporary_data['name']
        print(temporary_name)
        temporary_message = temporary_data['message']
        print(temporary_message)

        with sessionmaker(bind=ENGINE)() as session:
            message = ChatServerMessage(
                username = temporary_name,
                message = temporary_message
            )

            session.add(message)
            session.commit()

    # with ENGINE.connect() as con:
    #     query = "INSERT INTO chat_server_messages (username) VALUES ('rzud');"

    #     con.execute(query)
        # con.commit()


def insert_batch():
    """
    insert batch
    """

    ENGINE = chat_server_create_engine()

    with sessionmaker(bind=ENGINE)() as session:
        for count in range(1, 10):
            message = ChatServerMessage(
                username="rzu{}".format(count)
            )

            session.add(message)
        
        session.commit()


def update_one():
    ENGINE = chat_server_create_engine()

    with sessionmaker(bind=ENGINE)() as session:
        result = session.query(ChatServerMessage).filter(ChatServerMessage.username=='rzu').first()
        
        result.username = result.username + "x"

        session.add(result)
        session.commit()


def update_batch():
    pass


def delete_one():
    pass


def read_one() -> ChatServerMessage:
    ENGINE = chat_server_create_engine()

    with sessionmaker(bind=ENGINE)() as session:
        result: ChatServerMessage = session.query(ChatServerMessage).filter(ChatServerMessage.username=='rzu5').first()

        return result
