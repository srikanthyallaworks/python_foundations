#!/usr/bin/env python3

import sys

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

import http.server
import webbrowser

port = 8000
url = f'http://localhost:{port}'

def main(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving @{url}')
    webbrowser.open_new(url)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
