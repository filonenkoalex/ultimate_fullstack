from argparse import ArgumentParser
from fastapi import APIRouter, FastAPI
from uvicorn import run

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8080


class App:
    def __init__(self):
        self.health = APIRouter(prefix="/health")

    def setup(self):
        pass

    def __call__(self, host: str, port: int, *args, **kwds):
        app = FastAPI()

        app.include_router(router=self.health)
        run(app, host=host, port=port)


def main():
    parser = ArgumentParser(description="UltimateApp Framework")
    parser.add_argument("--host", help="Host address to use", default=DEFAULT_HOST)
    parser.add_argument("--port", help="Port to use", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()

    app = App()
    app.setup()
    app(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
