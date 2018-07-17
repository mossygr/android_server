import http.server
import socketserver
from requests import get


PORT = 8000
ip = get('https://api.ipify.org').text

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Visit the following url: ", ip, ":", PORT,sep='')
    httpd.serve_forever()


