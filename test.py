import argparse

parser = argparse.ArgumentParser(description='Start Chat Server')

# Add arguments to the parser
parser.add_argument('--host', type=str, default='localhost', help='Host address for the server')
parser.add_argument('--port', type=int, default=8080, help='Port number for the server')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the arguments
host = args.host
port = args.port
debug = args.debug

# Now you can use the values of these arguments in your script
print(f'Starting server on {host}:{port}{" in debug mode" if debug else ""}')
