import http.server

port = 8000

def main(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving @ http://localhost:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    main()
