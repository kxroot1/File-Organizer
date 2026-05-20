# Automated File Organizer CLI


A Python automation script that scans a specified directory and organizes disorganized files into structured folders based on their file extensions (e.g., Images, Documents, Videos). It helps keep your workspace clean and automates tedious manual sorting.


## Features


- **Multi-Category Sorting:** Maps specific file extensions to predefined destination folders.


- **Smart Folder Creation:** Dynamically checks if a category folder exists; if not, it automatically creates it on the fly using `os.makedirs`.


- **Fallback Mechanism (Others):** Unrecognized file extensions are safely moved into an `Others` folder instead of being ignored or left behind.


## Supported Categories


The script maps a wide array of formats, including:


- **Images:** `.jpg`, `.png`, `.svg`, `.gif`, etc.


- **Documents:** `.pdf`, `.docx`, `.xlsx`, `.txt`, etc.


- **Development & Data:** `.py`, `.html`, `.js`, `.json`, `.yaml`, etc.


- **Archives & Programs:** `.zip`, `.rar`, `.exe`, `.msi`, `.bat`, etc.

## How it Works


The script asks for a directory path, validates it, and processes the contents.


### Logic Breakdown


1. **Validation:** Checks if the provided input is a valid directory via `os.path.isdir()`.


2. **Scanning:** Loops over items inside the folder using `os.listdir()`, ignoring folders to only move actual files via `os.path.isfile()`.


3. **File Splitting:** Uses `os.path.splitext()` to safely separate filenames from their extensions.


4. **Relocation:** Uses `shutil.move()` to shift the file path directly into the matched category.


## How to Run


### Prerequisites
Make sure you have Python 3.x installed. (Uses standard libraries only, no external `pip` packages required).


### Steps


1. Save the code in a file named `main.py`.


2. Open your terminal or command prompt.


3. Run the script:
   ```bash
   python main.py
4.Enter the full path of the folder you want to clean up (e.g., C:\Users\Name\Downloads).
   
