from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response

from seamless.middlewares import ASGIMiddleware
from .common import index, css_file

HERE = Path(__file__).parent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    ASGIMiddleware,
)

app.get("/c", response_class=HTMLResponse)(index)
app.get("/static/main.css")(lambda: Response(css_file(), media_type="text/css"))
