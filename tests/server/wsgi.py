from flask import Flask
from jsx.middlewares import WSGIMiddleware
from .common import index, db_memory

app = Flask(__name__)
app.wsgi_app = WSGIMiddleware(app.wsgi_app)

app.get("/c")(index)
app.get("/usage")(db_memory)

def run():
    app.run(host="0.0.0.0", port=8081, debug=True)