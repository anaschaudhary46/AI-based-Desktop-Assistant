import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi, i am MARC. How may I assist you today?")

def takeCommand():
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
        print(e)
        print("Sorry, I couldn't understand your command.")
        return "None"
    return query


def playMusic():
    music_dir = 'C:\\Users\\Kaleem\\Documents\\Zapya\\Music'
    songs = os.listdir(music_dir)
    if songs:
        song_to_play = os.path.join(music_dir, random.choice(songs))
        os.system(f'start vlc "{song_to_play}"')
    else:
        speak("No music files found in the directory.")

def getWeather():
    # You can replace 'your_api_key' with a valid API key
    api_key = 'ff387bfbc7026236e54200226b51841b'
    city = 'Lahore'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        description = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temperature} degrees Celsius, with {description} and {humidity}% humidity.")
    else:
        speak("Sorry, I couldn't fetch the weather data for your city.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            if query:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)                 
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("It seems there are multiple matching results. Please specify your query.")
                except wikipedia.exceptions.PageError as e:
                    speak("I couldn't find any relevant information on Wikipedia for your query.")
            else:
                speak("I couldn't find any relevant information on Wikipedia for your query.")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com")

        elif 'play music' in query:
            playMusic()
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
           codePath = "C:\\Users\\Kaleem\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile (codePath)

        elif 'weather' in query:
            getWeather()

        