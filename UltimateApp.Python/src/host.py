import os
from api import app
from uvicorn import run
from argparse import ArgumentParser

DEFAULT_PORT = 8080
ENV_VARIABLE_PORT_NAME = "UVICORN_PORT"
DEFAULT_HOST = "127.0.0.1"
DESCRIPTION = "UltimateApp Framework"

def start():
    host = DEFAULT_HOST
    port = os.environ.get(ENV_VARIABLE_PORT_NAME, DEFAULT_PORT)
    
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("--host", help="Host address to use", default=host)
    parser.add_argument("--port", help="Port to use", type=int, default=port)
    
    args = parser.parse_args()

    run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    start()
