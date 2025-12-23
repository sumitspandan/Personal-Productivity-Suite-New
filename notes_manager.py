import json
import os
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "notes.json")


class NotesManager:
    def __init__(self):
        # Ensure data directory exists
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    self.notes = json.load(f)
            else:
                self.notes = []
        except json.JSONDecodeError:
            # If file is corrupted or empty
            self.notes = []

    def save_notes(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self):
        title = input("Enter note title: ").strip()
        content = input("Enter note content: ").strip()

        if not title or not content:
            print("❌ Title and content cannot be empty!")
            return

        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.notes.append(note)
        self.save_notes()
        print("✅ Note added successfully!")

    def view_notes(self):
        if not self.notes:
            print("No notes found.")
            return

        for note in self.notes:
            print("\n----------------------")
            print(f"ID      : {note['id']}")
            print(f"Title   : {note['title']}")
            print(f"Content : {note['content']}")
            print(f"Created : {note['created']}")

    def run(self):
        while True:
            print("\nNOTES MANAGER")
            print("1. View Notes")
            print("2. Add Note")
            print("3. Back")

            choice = input("Choose: ")

            if choice == '1':
                self.view_notes()
            elif choice == '2':
                self.add_note()
            elif choice == '3':
                break
            else:
                print("❌ Invalid choice. Try again.")
