from http import server

class GodotRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # These headers are MANDATORY for Godot 4 Web builds
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

print("Starting Godot Local Server on http://localhost:8000")
server.test(HandlerClass=GodotRequestHandler, port=8000)
