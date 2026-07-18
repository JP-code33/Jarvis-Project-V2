import speech_recognition as sr
import webbrowser
import pyttsx3

recognizaer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

if __name__ == "__main__":
    speak("Intitializing Jarvis....")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Lsitening...")
            audio = r.listen(source, timeout=2)
        

        try:
            command = r.recognize_google(audio)
            print (command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
