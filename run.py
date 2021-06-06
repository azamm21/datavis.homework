import http.server
import socketserver

PORT = 8000


Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", '127.0.0.1:' + str(PORT))
    print("serving at port", PORT)

    httpd.serve_forever()
