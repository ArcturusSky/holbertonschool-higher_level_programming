#!/usr/bin/python3
"""
Module to start Develop a simple API using Python with the `http.server` module
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """
    Subclass to config a HTTP server
    """

    def do_GET(self):
        """
        Function to manage Get request
        """

        if self.path == '/':
            self.send_response(200)  # 200 OK
            self.send_header('Content-type', 'text/plain')  # Type de contenu
            self.end_headers()  # Fin des en-têtes
            self.wfile.write(b'Hello, this is a simple API!')
            # Réponse aux client avec "b" pour byte, requis pour écrire la réponse

        elif self.path == '/data':
            self.send_response(200)  # 200 OK
            self.send_header('Content-type', 'application/json')  # Type de contenu JSON
            self.end_headers()  # Fin des en-têtes
            # Créer un dictionnaire et le convertir en JSON
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())  # Écrire la réponse en JSON

        elif self.path == '/info':
            self.send_response(200)  # 200 OK
            self.send_header('Content-type', 'application/json')  # Type de contenu JSON
            self.end_headers()  # Fin des en-têtes
            # Créer un dictionnaire et le convertir en JSON
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode())  # Écrire la réponse en JSON

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


# Function pour démarrer le serveur
def run(server_class=HTTPServer, handler_class=SimpleAPI, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
