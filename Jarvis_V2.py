import speech_recognition as sr
import webbrowser
import os
from dotenv import load_dotenv
from groq import Groq
import win32com.client

load_dotenv()
recognizaer = sr.Recognizer()
#engine = pyttsx3.init()

def speak(text):
    if not text:
        return
    print(f"Jarvis: {text}")
    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)
    except Exception as e:
        print(f"[Speech Error]: {e}")

def aiCommand(command):
    try:
        secret_key = os.getenv("GROQ_API_KEY")

        if not secret_key:
            print("Error: GROQ_API_KEY is not set or .env file wasn't found.")
            return "My key configuration is missing, Sir."
        
        client = Groq(api_key=secret_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a virtual asistant named Jarvis skilled in general tasks. Respond the questions."
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq API Eror: {e}")
        return "My network paths are currently offline, Sir!"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    else:
        speak("Consulting artificial intelligence core...")
        

        ai_reply = aiCommand(c)

        speak(ai_reply)
      
 

if __name__ == "__main__":

    speak("Initializing Jarvis....")

    r = sr.Recognizer()
    
    # Adjust microphone for ambient noise once at the start
    with sr.Microphone() as source:
        print("[DEBUG] Calibrating microphone for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("[DEBUG] Microphone calibrated.")

    while True:
        r = sr.Recognizer()

        print("recongnizing...")        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))        

