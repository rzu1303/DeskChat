Project Name: DESKChat  

Overview:  
DESKChat is a real-time chat server application that allows multiple clients to connect, send, and receive messages. It is implemented in Python and uses PostgreSQL for message storage. The server listens for incoming client connections, manages the communication between connected clients, and ensures all messages are broadcasted to every client. The server also supports basic database operations such as inserting and reading messages to and from the database.   

Key components of DESKChat:  
Client Connection Management: Accepts multiple client connections and handles message broadcasting.  
Database Operations: Stores messages in a PostgreSQL database and provides functions for inserting and reading messages.    

Logging: Provides detailed logging of server activities for easier debugging and monitoring.  
Configuration Management: Uses a configuration file to manage database and server settings, making it easy to customize the setup.

Features:  
Handles multiple client connections.  
Broadcasts messages to all connected clients.  
Stores chat messages in a PostgreSQL database.
Supports basic database operations like insert, update, and read.    

Usage:  
To start the chat server, run the __main__.py file with an optional configuration file argument.    

Database Setup:  
The server uses PostgreSQL to store chat messages. Ensure that you have PostgreSQL installed and running. The database schema is defined in chat_server/models/create.py.    

Logging:  
Logging is configured to output both to the console and to a file. The log configuration is defined in chat_server/logger.py. Logs are stored in the logs directory by default.  
