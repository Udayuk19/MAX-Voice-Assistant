# MAX-Voice-Assistant

MAX-Voice-Assistant is a Python desktop assistant that listens to your voice commands and responds with both text and speech.  
It can play music, answer questions, tell jokes, search the web, provide weather updates, perform calculations, and more.

## Features

- Play songs on YouTube
- Tell the current time
- Answer "Who is" questions using Wikipedia
- Tell jokes
- Respond with its name ("What is your name?")
- Open Chrome and VS Code
- Search Google
- Provide weather information (OpenWeatherMap API required)
- Perform math calculations
- Give system/computer info
- Exit on command

## Requirements

- Python 3.10+
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`
- `pyjokes`
- `requests`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Replace `"your_openweathermap_api_key"` in `assistant.py` with your actual OpenWeatherMap API key for weather features.
2. Run the assistant:
   ```bash
   python assistant.py
   ```
3. Speak your command when prompted.

## Example Commands

- "Play Shape of You"
- "What's the time?"
- "Who is Elon Musk?"
- "Tell me a joke"
- "Open Chrome"
- "Search Python tutorials"
- "Weather in Hyderabad"
- "Calculate 25 plus 17"
- "What is your name?"
- "System info"
- "Exit"

---

**MAX** will listen, display your command, and respond
