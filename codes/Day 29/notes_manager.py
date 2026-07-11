"""File-backed note storage."""

from pathlib import Path


class NotesManager:
    """Save and retrieve plain-text notes, one note per line."""

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def add(self, note: str) -> None:
        """Append a non-empty note to the storage file."""
        with self.file_path.open("a", encoding="utf-8") as notes_file:
            notes_file.write(note.replace("\n", " ") + "\n")

    def get_all(self) -> list[str]:
        """Return saved notes, excluding blank lines."""
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as notes_file:
            return [line.strip() for line in notes_file if line.strip()]
