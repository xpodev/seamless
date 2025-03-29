from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from seamless import render
from seamless.middlewares import SocketIOMiddleware

from components.app import App

from seamless.context import get_context
from pydom.context.standard.transformers.class_transformer import ClassTransformer

class_transformer = next(t for t in get_context().prop_transformers if isinstance(t, ClassTransformer))
if class_transformer:
    class_transformer.prop_name = "classes"

HERE = Path(__file__).parent

app = FastAPI()
app.add_middleware(SocketIOMiddleware)


@app.get("/static/{file_path:path}")
def read_static(file_path: str):
    return FileResponse(HERE / "static" / file_path)


@app.get("/favicon.ico")
def read_favicon():
    favicon = HERE / "static" / "favicon.ico"
    if favicon.exists():
        return FileResponse(favicon)
    
    return ""


@app.get("/{full_path:path}", response_class=HTMLResponse)
def read_root():
    return render(App())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
