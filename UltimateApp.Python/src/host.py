from argparse import ArgumentParser
from api import app
from uvicorn import run

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8080


def start():
    parser = ArgumentParser(description="UltimateApp Framework")
    parser.add_argument("--host", help="Host address to use", default=DEFAULT_HOST)
    parser.add_argument("--port", help="Port to use", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()

    run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    start()
