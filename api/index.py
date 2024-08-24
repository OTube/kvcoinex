from http.server import BaseHTTPRequestHandler
lots={}
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(self.path.encode('utf-8'))
        op=self.path.split("op")[1]
        if op=="setlot":
            token=self.path.split("token")[1]
            value=self.path.split("value")[1]
            lots[token]=value
        if op=="getlot":
            token=self.path.split("token")[1]
            if token in lots:
                self.wfile.write(str(lots[token]).encode('utf-8'))
                del lots[token]
            else:
                self.wfile.write("error".path.encode('utf-8'))
        if op=="checkstatus":
            if token in lots:
                self.wfile.write("yes".encode('utf-8'))
            else:
                self.wfile.write("no".path.encode('utf-8'))
