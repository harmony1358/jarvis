from flask import Flask, jsonify, request
from jarvis.jarvis import Jarvis

class JarvisServer:

    def __init__(self, key, user, assistant):
        self.app = Flask(__name__)
        self.routes()
    
        self.jarvis = Jarvis(key, user, assistant)

    def routes(self):

        @self.app.route("/respond", methods=["POST"])
        def respond():
            prompt = request.json.get("prompt")
            response = self.jarvis.respond(prompt)
            return jsonify({"message": response})
        
        @self.app.route("/reset", methods=["GET"])
        def reset():
            self.jarvis.reset()
            return jsonify({"message": "OK"})

    def run(self):
        self.app.run()
