import configparser
import logging
from jarvis.jarvis import Jarvis
import speech_recognition as sr
import pyttsx3

logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('server.ini')

key = config.get("jarvis", "key")
user = config.get("jarvis", "user")
assistant = config.get("jarvis", "assistant")

jarvis = Jarvis(key, user, assistant)

engine = pyttsx3.init()
r = sr.Recognizer()

while True:
    user_input = input("Press RETURN key to start the conversation\n")
    with sr.Microphone() as source:
        print("Ask something in polish\n")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recognized_text = r.recognize_google(audio, language='pl-PL')
        print(f"You said: {recognized_text}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

    response = jarvis.respond(recognized_text)
    engine.say(response)
    engine.runAndWait()
