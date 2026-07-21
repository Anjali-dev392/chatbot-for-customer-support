import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from chatbot import get_response


class ChatbotHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            html_path = Path(__file__).resolve().parent / "index.html"
            self.wfile.write(html_path.read_bytes())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_POST(self):
        if self.path != "/chat":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        try:
            payload = json.loads(body) if body else {}
        except json.JSONDecodeError:
            payload = {}

        message = payload.get("message", "")
        response_text = get_response(message)

        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({"response": response_text}).encode("utf-8"))

    def log_message(self, format, *args):
        return


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 8000), ChatbotHandler)
    print("Chatbot server running at http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
