import configparser
import logging
from jarvis.jarvis_server import JarvisServer

logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('server.ini')

key = config.get("jarvis", "key")
user = config.get("jarvis", "user")
assistant = config.get("jarvis", "assistant")

server = JarvisServer(key, user, assistant)
server.run()
