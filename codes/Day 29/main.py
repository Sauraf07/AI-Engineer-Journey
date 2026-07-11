"""Entry point for the Personal Assistant command-line application."""

from assistant import PersonalAssistant


def main() -> None:
    """Start the application."""
    PersonalAssistant().run()


if __name__ == "__main__":
    main()
