from http.server import BaseHTTPRequestHandler
lots=[-1]*1000
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        if self.path.count("op")<2:
            self.wfile.write("forbidden".encode('utf-8'))
            return
        op=self.path.split("op")[1]
        if op=="setlot":
            if self.path.count("token")<2:
                self.wfile.write("forbidden".encode('utf-8'))
                return
            token=self.path.split("token")[1]
            if len(token)!=6 not is_numeric(token):
                self.wfile.write("forbidden".encode('utf-8'))
                return
            if self.path.count("value")<2:
                self.wfile.write("forbidden".encode('utf-8'))
                return
            value=self.path.split("value")[1]
            if not is_numeric(value):
                self.wfile.write("forbidden".encode('utf-8'))
                return
            lots[int(token)]=int(value)
        elif op=="getlot":
            if self.path.count("token")<2:
                self.wfile.write("forbidden".encode('utf-8'))
                return
            if not is_numeric(token):
                self.wfile.write("forbidden".encode('utf-8'))
                return
            token=self.path.split("token")[1]
            if len(token)!=6 not is_numeric(token):
                self.wfile.write("forbidden".encode('utf-8'))
                return
            if lots[int(token)]!=-1:
                self.wfile.write(lots[token].encode('utf-8'))
                lots[int(token)]=-1
            else:
                self.wfile.write("error".encode('utf-8'))
        else:
            self.wfile.write("forbidden".encode('utf-8'))
