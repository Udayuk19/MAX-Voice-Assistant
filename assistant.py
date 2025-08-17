import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import webbrowser
import platform
import requests

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def talk(text):
    print("🎙️ NOVA:", text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")    
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def get_weather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return "Sorry, I couldn't find weather info for that city."
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    except:
        return "Sorry, I couldn't get the weather information."

def calculate(expression):
    try:
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "Sorry, I couldn't calculate that."

def run_nova():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "what is your name" in command or "who are you" in command:
        talk("My name is MAX, your personal voice assistant.")

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "search" in command:
        query = command.replace("search", "").strip()
        talk(f"Searching for {query} on Google 🌐")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "weather in" in command:
        city = command.split("weather in")[-1].strip()
        weather_info = get_weather(city)
        talk(weather_info)

    elif "calculate" in command:
        expression = command.replace("calculate", "").strip()
        answer = calculate(expression)
        talk(answer)

    elif "system info" in command or "computer info" in command:
        info = f"System: {platform.system()}, Release: {platform.release()}, Version: {platform.version()}, Processor: {platform.processor()}"
        talk(info)

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        try:
            info = wikipedia.summary(query, sentences=2)
            talk(info)
        except:
            talk("Sorry, I couldn't find anything on Wikipedia.")

    elif "exit" in command or "stop" in command:
        talk("Okay, see you later 👋")
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")

talk("Yo! I'm MAX – your personal voice assistant 💡")
while True:
    run_nova()