import argparse
import uvicorn

args = argparse.ArgumentParser()
args.add_argument("--type", action="store", type=str, default="asgi")

args = args.parse_args()


if __name__ == "__main__":
    if args.type == "asgi":
        uvicorn.run("tests.server.asgi:app", host="0.0.0.0", reload=True, port=8081)
    elif args.type == "manual":
        uvicorn.run("tests.manual:app", host="0.0.0.0", reload=True, port=8081)
