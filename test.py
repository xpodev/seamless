import uvicorn

if __name__ == "__main__":
  uvicorn.run("tests.server:app", host="0.0.0.0", reload=True, port=8081)