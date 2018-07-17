from requests import get
import http.server
import socketserver


ip = get('https://api.ipify.org').text
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    
    httpd.serve_forever()
httpd.serve_forever()

print ("serving at ",ip,":", PORT)
