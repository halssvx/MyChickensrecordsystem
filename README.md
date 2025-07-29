🐔 MyChickensRecordSystem — Chicken-UI PID
Overview
Chicken-UI PID is a command-line interface (CLI) application built in Python to help a local chicken breeder manage their chicken records. This is a Proof of Concept (PoC) designed to demonstrate how a paper-based system can be replaced with a simple, local digital solution.

✅ Features
Text-based interactive menu

In-memory chicken record management

Clean and modular code using Python functions

Input validation and user-friendly messages

Lightweight and portable (no dependencies)

🧠 What You Can Do
View a list of chickens

Add a new chicken record

Update an existing chicken's name

Delete a chicken record

Exit the application

📦 Requirements
Python 3.x

Runs in terminal (Windows, macOS, Linux)

No third-party libraries required

📁 Installation
🔽 Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/chicken-ui-pid.git
cd chicken-ui-pid
🐍 Run the Application
bash
Copy
Edit
python chicken_ui.py
🐳 Docker Support
You can also run the app inside a Docker container.

🛠️ Build the Docker Image
bash
Copy
Edit
docker build -t chicken_app .
▶️ Run the Container
bash
Copy
Edit
docker run -it --rm chicken_app
This runs the app interactively in a clean environment with Python 3.11 installed.

📂 Code Structure
chicken_ui.py
Function	Description
print_menu()	Displays the main menu options
print_chickens()	Lists all current chicken records
add_chicken()	Adds a new chicken to the list
update_chicken()	Updates the name of an existing chicken
delete_chicken()	Deletes a chicken by index
main()	Runs the interactive menu loop

Data Structure
python
Copy
Edit
chickens = ["George", "Fleur", "Devon", "Casey", "Marigold", "Apple Mint"]
🛠️ Planned Enhancements
 Save/load records from a .csv file

 Add search functionality

 Add backup/restore feature

 Add GUI (e.g., Tkinter or PySimpleGUI)

 Add unit tests

📝 License
This project is open-source and free to use for educational or personal purposes.

👩‍💻 Author
Developed as a learning project to practice:

Python fundamentals

Functions and conditionals

Loops and list operations

CLI interaction

Docker basics (containerization, image building, etc.)

