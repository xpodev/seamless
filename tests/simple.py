from http.server import BaseHTTPRequestHandler, HTTPServer

from pydom import render, Div
from pydom.page import Page


def index():
    return Page(title="Hello, world!")(
        Div(classes=["a", "b"])("Hello, world!")
    )


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(render(index()).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
