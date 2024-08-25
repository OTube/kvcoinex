from http.server import BaseHTTPRequestHandler
lots={}
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        if self.path.count("op")<2:
            self.wfile.write("forbidden".encode('utf-8'))
            return
        op=self.path.split("op")[1]
        self.wfile.write(op.encode('utf-8'))
