from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()


if __name__ == '__main__':
    http_server = HTTPServer(('0.0.0.0', 80), HTTPRequestHandler)
    http_server.serve_forever()
