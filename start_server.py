import http.server
import socketserver
import os
import time

# GITHUB SOLUTION

# make server for p5js to make library
PORT = 8000
web_dir = os.path.dirname(__file__)
os.chdir(web_dir)
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
print("serving at port", PORT)
# httpd.serve_forever(poll_interval=10)
# time.sleep(10)
# httpd.shutdown()

def serve():
    httpd.serve_forever()

