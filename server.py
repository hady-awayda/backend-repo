# repo_B/server.py
from config_reader import read_config

config = read_config()

run_localhost = config.get('run_localhost', False)
server_host = config.get('server_host', 'localhost')
server_port = config.get('server_port', 8080)

if run_localhost:
    print("Running on localhost")
    # Your code to handle localhost logic

print(f"Server will run on {server_host}:{server_port}")
# Your server logic here
