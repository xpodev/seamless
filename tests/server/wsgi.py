from flask import Flask, Response
from jsx.middlewares import WSGIMiddleware
from .common import index, db_memory, css_file

app = Flask(__name__)
app.wsgi_app = WSGIMiddleware(app.wsgi_app)

app.get("/c")(index)
app.get("/usage")(db_memory)
app.get("/static/main.css")(lambda: Response(css_file(), content_type="text/css"))

def run():
    app.run(host="0.0.0.0", port=8081, debug=True)