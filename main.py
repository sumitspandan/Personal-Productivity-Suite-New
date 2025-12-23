from calculator import Calculator
from notes_manager import NotesManager
from timer import TimerTool
from file_organizer import FileOrganizer
from unit_converter import UnitConverter
from utils import clear_screen, pause

def main():
    while True:
        clear_screen()
        print("=" * 45)
        print("     PERSONAL PRODUCTIVITY SUITE")
        print("=" * 45)

        print("""
1. Calculator Tool
2. Notes Manager
3. Timer
4. File Organizer
5. Unit Converter
6. Exit
""")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            Calculator().run()
        elif choice == '2':
            NotesManager().run()
        elif choice == '3':
            TimerTool().run()
        elif choice == '4':
            FileOrganizer().run()
        elif choice == '5':
            UnitConverter().run()
        elif choice == '6':
            print("Goodbye!")
            break

        pause()

if __name__ == "__main__":
    main()
