from http.server import BaseHTTPRequestHandler
lots={}
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("forbidden".encode('utf-8'))
        return
