import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Edith Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia...", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            speak("Playing song...")
            # print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%B %d, %Y")
            # strDate = datetime.datetime.now().strftime("%b-%d-%Y")
            print(f"Sir, the date is {strDate}")
            speak(f"Sir, the date is {strDate}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\dipak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("opening vs code...")
            speak("opening vs code...")
            os.startfile(codePath)

        elif 'open vlc' in query:
            vlcPath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            print("opening vlc media player...")
            speak("opening vlc media player...")
            os.startfile(vlcPath)
