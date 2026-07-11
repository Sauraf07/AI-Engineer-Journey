# Personal Assistant

A menu-driven Python command-line application with a calculator, file-backed notes manager, current date and time, motivational quotes, and live weather information.

## Features

- Calculator: add, subtract, multiply, and divide with input validation.
- Notes manager: save notes to `notes.txt` and view them later.
- Weather: retrieves temperature, humidity, and weather condition for any city through the free Open-Meteo REST APIs (no API key required).
- Date and time: displays the local system date and time.
- Safe error handling for invalid input, file errors, and API/network problems.

## Project structure

```
Personal-Assistant/
├── main.py             # Application entry point
├── assistant.py        # Menu and feature coordination
├── calculator.py       # Reusable calculator logic
├── notes_manager.py    # File-backed note operations
├── weather.py          # REST API client
├── notes.txt           # Saved notes
├── requirements.txt
└── README.md
```

## Setup and run

```bash
python -m venv .venv
.venv\\Scripts\\activate       # Windows PowerShell
pip install -r requirements.txt
python main.py
```

The weather feature needs an internet connection. All other features work offline.
