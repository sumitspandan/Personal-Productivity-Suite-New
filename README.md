📌 Personal Productivity Suite (Python CLI Application)
📖 Project Overview
The Personal Productivity Suite is a menu-driven command-line application developed using Python, designed to combine multiple everyday productivity tools into a single, unified interface.
This project focuses on simplicity, modularity, and usability, allowing users to perform common tasks efficiently from the terminal without installing heavy software or graphical applications.
🎯 Objectives of the Project
To build a single platform that offers multiple productivity utilities
To practice modular programming using Python classes and files
To demonstrate file handling, user input handling, and control flow
To provide a beginner-friendly CLI tool that is easy to understand and extend
🧩 Features Included
🧮 Calculator Tool – Performs basic arithmetic operations
📝 Notes Manager – Allows users to create and view notes stored in JSON format
⏲ Timer – Executes a countdown timer for a specified duration
📂 File Organizer – Automatically organizes files into folders based on file extensions
🔁 Unit Converter – Converts kilometers into meters and miles
🚪 Exit Option – Safely exits the application
Each feature is implemented as an independent module, making the project easy to maintain and scalable for future enhancements.
⚙️ Setup Instructions
Follow the steps below to run the project successfully on your system.
✅ Prerequisites
Python 3.8 or higher
Any operating system (Windows / macOS / Linux)
Basic knowledge of terminal or command prompt
📁 Project Structure
personal_productivity_suite/
│
├── main.py
├── calculator.py
├── notes_manager.py
├── timer.py
├── file_organizer.py
├── unit_converter.py
├── utils.py
│
├── data/
│   └── notes.json
│
└── README.md
🚀 Installation & Execution Steps
Clone the repository
git clone https://github.com/your-username/personal_productivity_suite.git
Navigate to the project directory
cd personal_productivity_suite
(Optional) Create the data folder
mkdir data
Run the application
python main.py
🖥 How to Use the Application
After running main.py, a menu will appear.
Enter a number between 1–6 to select a tool.
Follow the on-screen prompts to use the selected functionality.
Press Enter when prompted to return to the main menu.
Select 6 to exit the application.
🛠 Technologies Used
Python 3
Standard Python libraries:
os
json
time
datetime
shutil
🔮 Future Improvements
Add delete/edit functionality in Notes Manager
Support more unit conversions
Add error handling and input validation
Convert CLI into a GUI application
Store logs and user activity
👨‍💻 Author
Sumit Spandan
Personal Productivity Suite – Python Project
