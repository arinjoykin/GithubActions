from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/hello':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"message": "Hello World"})
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 5000), HelloHandler)
    print('Server running on port 5000...')
    server.serve_forever()