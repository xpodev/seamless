from socketio import Server, WSGIApp

from .base import BaseMiddleware

class WSGIMiddleware(BaseMiddleware):
    def __call__(self, env, start_response):
        return self.app(env, start_response)
    
    def _app_class(self):
        return WSGIApp
    
    def _server_class(self):
        return Server