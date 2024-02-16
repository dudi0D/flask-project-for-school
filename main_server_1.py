
from http.server import HTTPServer, CGIHTTPRequestHandler

print("http://localhost:8000/")
print("http://localhost:8000/cgi-bin/index.py")
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
