#!/usr/bin/env python3

import sys
import http.server
import socketserver
import webbrowser

port = 8000
directory = "www"
url = f'http://localhost:{port}'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)


def main():
    print(f'Serving @{url}')
    webbrowser.open_new(url)
    with socketserver.TCPServer(("", port), Handler) as httpd:
    	httpd.serve_forever()

    	
if __name__ == "__main__":
    main()
