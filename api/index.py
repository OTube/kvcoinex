from http.server import BaseHTTPRequestHandler
lots={}
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("forbidden".encode('utf-8'))
        return
        if self.path.count("op")<2:
            self.wfile.write("forbidden".encode('utf-8'))
            return
        op=self.path.split("op")[1]
        if op=="setlot":
            if self.path.count("token")<2:
                self.wfile.write("forbidden".encode('utf-8'))
                return
            token=self.path.split("token")[1]
            if self.path.count("value")<2:
                self.wfile.write("forbidden".encode('utf-8'))
                return
            value=self.path.split("value")[1]
            lots[token]=value
        else if op=="getlot":
            if self.path.count("token")<2:
                self.wfile.write("forbidden".encode('utf-8'))
                return
            token=self.path.split("token")[1]
            if token in lots:
                self.wfile.write(str(lots[token]).encode('utf-8'))
                del lots[token]
            else:
                self.wfile.write("error".encode('utf-8'))
        else if op=="checkstatus":
            if token in lots:
                self.wfile.write("yes".encode('utf-8'))
            else:
                self.wfile.write("no".encode('utf-8'))
        else:
            self.wfile.write("forbidden".encode('utf-8'))
