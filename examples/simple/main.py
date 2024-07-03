from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from seamless import render
from seamless.middlewares import ASGIMiddleware

from pages.home import HomePage
from pages.counter import CounterPage

HERE = Path(__file__).parent

app = FastAPI()
app.add_middleware(ASGIMiddleware)


@app.get("/", response_class=HTMLResponse)
def read_root():
    return render(HomePage())


@app.get("/counter", response_class=HTMLResponse)
def read_root():
    return render(CounterPage())


@app.get("/static/{file_path:path}")
def read_static(file_path: str):
    return FileResponse(HERE / "static" / file_path)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
