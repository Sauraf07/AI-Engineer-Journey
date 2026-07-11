"""Menu and user-interface code for the Personal Assistant."""

from datetime import datetime
from pathlib import Path
import random

from calculator import calculate_from_input
from notes_manager import NotesManager
from weather import WeatherService


QUOTES = (
    "The best way to predict the future is to create it.",
    "Small progress every day adds up to big results.",
    "Success is the sum of small efforts repeated daily.",
)


class PersonalAssistant:
    """Coordinate the assistant's interactive features."""

    def __init__(self) -> None:
        self.notes = NotesManager(Path(__file__).with_name("notes.txt"))
        self.weather = WeatherService()

    def run(self) -> None:
        """Display the menu until the user exits."""
        print("\nWelcome to your Personal Assistant!")
        print(f'\"{random.choice(QUOTES)}\"')
        while True:
            self._display_menu()
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self._calculator()
            elif choice == "2":
                self._add_note()
            elif choice == "3":
                self._view_notes()
            elif choice == "4":
                self._show_weather()
            elif choice == "5":
                self._show_date_time()
            elif choice == "6":
                print("Goodbye! Have a great day.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

    @staticmethod
    def _display_menu() -> None:
        print("\n" + "=" * 30)
        print("      PERSONAL ASSISTANT")
        print("=" * 30)
        print("1. Calculator")
        print("2. Add Note")
        print("3. View Notes")
        print("4. Weather")
        print("5. Date & Time")
        print("6. Exit")

    @staticmethod
    def _calculator() -> None:
        print("\n--- Calculator ---")
        print("Operations: +  -  *  /")
        try:
            result = calculate_from_input()
            print(f"Result = {result}")
        except ValueError as error:
            print(f"Calculator error: {error}")

    def _add_note(self) -> None:
        print("\n--- Add Note ---")
        note = input("Enter note: ").strip()
        if not note:
            print("A note cannot be empty.")
            return
        try:
            self.notes.add(note)
            print("Note saved successfully!")
        except OSError as error:
            print(f"Could not save the note: {error}")

    def _view_notes(self) -> None:
        print("\n--- Notes ---")
        try:
            notes = self.notes.get_all()
        except OSError as error:
            print(f"Could not read notes: {error}")
            return
        if not notes:
            print("No notes saved yet.")
            return
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")

    def _show_weather(self) -> None:
        print("\n--- Weather ---")
        city = input("Enter city: ").strip()
        if not city:
            print("City name cannot be empty.")
            return
        try:
            weather = self.weather.get_weather(city)
            print(f"City: {weather['city']}")
            print(f"Temperature: {weather['temperature']:.1f}\N{DEGREE SIGN}C")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Condition: {weather['condition']}")
        except RuntimeError as error:
            print(f"Weather unavailable: {error}")

    @staticmethod
    def _show_date_time() -> None:
        now = datetime.now()
        print("\n--- Current Date & Time ---")
        print(now.strftime("%d %B %Y"))
        print(now.strftime("%I:%M %p"))
