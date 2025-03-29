from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from seamless import render
from seamless.middlewares import SocketIOMiddleware

from components.app import App

HERE = Path(__file__).parent

app = FastAPI()
app.add_middleware(SocketIOMiddleware)


@app.get("/static/{file_path:path}")
def read_static(file_path: str):
    return FileResponse(HERE / "static" / file_path)


@app.get("/{full_path:path}", response_class=HTMLResponse)
def read_root():
    return render(App())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
