from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from seamless import render, Script
from seamless.middlewares import ASGIMiddleware
from seamless.rendering.transformers import post_render_transformer

from components.app import App
from seamless.rendering.tree.nodes.context_node import ContextNode

HERE = Path(__file__).parent

app = FastAPI()
app.add_middleware(ASGIMiddleware)

@post_render_transformer()
def script_head(root: ContextNode):
    head = root.get_by_tag("head")
    if head:
        head.append_child(Script(src="/static/script.js"))

@app.get("/static/{file_path:path}")
def read_static(file_path: str):
    return FileResponse(HERE / "static" / file_path)


@app.get("/{full_path:path}", response_class=HTMLResponse)
def read_root():
    return render(App())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
