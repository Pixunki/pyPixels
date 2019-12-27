from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import http.server
import socketserver

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', 8123)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
