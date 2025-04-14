import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Dictionary of commands and corresponding URLs
commands = {
    "open google": "https://www.google.com",
    "open youtube": "https://www.youtube.com",
    "open facebook": "https://www.facebook.com",
    "open twitter": "https://www.twitter.com",
    "open github": "https://www.github.com"
}

if __name__ == "__main__":
    speak("Initializing Maharaz....")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                command = r.recognize_sphinx(audio).lower()
                print(command)
                
                if command in commands:
                    url = commands[command]
                    webbrowser.open(url)
                    speak(f"Opening {command.split()[1]}")
                else:
                    speak("Command not recognized")
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
                speak("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
                speak("Sorry, there was an error with the speech recognition service.")