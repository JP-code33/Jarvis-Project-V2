import speech_recognition as sr
import webbrowser
import pyttsx3
import os
from dotenv import load_dotenv
from google import genai

load_dotenv
recognizaer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiCommand(command):
    try:
        secret_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=secret_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"System instruction: You are a virtual assistant named Jarvis skilled in general tasks. Respond in one short sentence: {command}"
        )
        return response.text
    except Exception as e:
        return "My network paths are currently offline, Sir!"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    else:
        engine.say("Consulting artiflicial intelligence core...")
        engine.runAndWait

        ai_reply = aiCommand(c)

        engine.say(ai_reply)
        engine.runAndWait
 

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()

        print("recongnizing...")        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                engine.say("Yes Sir")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

            