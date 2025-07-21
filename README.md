# MyChickensrecordsystem
# Chicken-UI PID

## Overview

**Chicken-UI PID** is a command-line interface (CLI) application built in Python to help a local chicken breeder manage their chicken records. This is a **Proof of Concept (POC)** designed to demonstrate how a paper-based system can be replaced with a simple, local digital solution.

The system allows users to:
- View a list of chickens
- Add a new chicken record
- Update an existing chicken’s name
- Delete a chicken record
- Exit the application

The data is stored in memory using a Python list while the program runs. The current version does not store data after the program ends, but file storage (e.g., CSV) can be added as an enhancement.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Planned Enhancements](#planned-enhancements)
- [License](#license)

---

## Features

- Text-based interactive menu
- In-memory data management
- Clean structure using functions
- Input validation and user-friendly prompts

---

## Requirements

- Python 3.x
- Works on Windows, Mac, and Linux terminals

No third-party libraries are required.

---

## Installation

1. Download or clone the repository:
   ```bash
   git clone https://github.com/your-username/chicken-ui-pid.git
   cd chicken-ui-pid
Save the following file to the project folder:

chicken_ui.py (main application)

Usage
To run the application:
Open a terminal or command prompt.

Navigate to the folder containing chicken_ui.py.

Run the script:

bash
Copy
Edit
python chicken_ui.py
Menu Options:
pgsql
Copy
Edit
Chicken Record System
0 - Exit App
1 - Print List of Chicken Records
2 - Create New Chicken Record
3 - Update Existing Chicken Record
4 - Delete a Chicken Record
Example Flow:
Choose option 1 to view current chickens.

Choose option 2 and type a name to add a new record.

Choose option 3 to update a specific chicken.

Choose option 4 to delete a chicken by number.

Code Structure
Copy
Edit
chicken_ui.py
Functions:
print_menu() – Displays the options to the user

print_chickens() – Lists all chickens

add_chicken() – Adds a new chicken to the list

update_chicken() – Edits a chicken's name

delete_chicken() – Removes a chicken from the list

main() – Runs the menu loop

Data Structure:
A simple Python list:

python
Copy
Edit
chickens = ["George", "Fleur", "Devon", "Casey", "Marigold", "Apple Mint"]
Planned Enhancements
Save and load chicken records from a .csv file

Add search functionality

Add file-based backup and restore

Add basic GUI using tkinter or PySimpleGUI (optional)

Add unit tests for core functions

License
This project is open-source and free to use for educational or personal purposes.

Author
Developed as part of a learning exercise to demonstrate Python fundamentals including:

Conditionals

Functions

Scope

Arrays (lists)

Loops and iteration

yaml
Copy
Edit

---

Let me know if you'd like to include:
- Screenshots or terminal output
- Contribution instructions
- GitHub badges (for online projects)
