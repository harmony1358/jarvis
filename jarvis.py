import pyttsx3
import openai
import logging
import speech_recognition as sr

logging.basicConfig(level=logging.DEBUG)
openai.api_key = "PUT YOUR API KEY HERE"

conversation=messages=[
            {"role": "user", "content": "Cześć, będziemy rozmawiali po polsku."},
            {"role": "assistant", "content": "OK"}
        ]

def jarvis_respond(prompt):

    conversation.append({"role": "user", "content": prompt});

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    response = chat.choices[0].message.content;
    conversation.append({"role": "assistant", "content": response});
    return response
engine = pyttsx3.init()
r = sr.Recognizer()

while True:
    user_input = input("Press any key to start the conversation")
    with sr.Microphone() as source:
        print("Ask something in polish")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recognized_text = r.recognize_google(audio, language='pl-PL')
        print(f"You said: {recognized_text}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

    response = jarvis_respond(recognized_text)
    engine.say(response)
    engine.runAndWait()
