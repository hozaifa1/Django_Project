# Django_Project
Overview:
This project is a Django-powered discussion forum that allows users to create accounts, post threads, and participate in discussions. The application provides a user-friendly interface for viewing and creating posts, and it allows users to search for posts by keyword. The project contains three Django apps: accounts, forum, and pages.

Requirements:
Before running the project, ensure that the following requirements are met:

1. Python 3.7 or later
2. Django 3.2 or later
3. A working internet connection

Installation:
Follow the steps below to run the project:

1.	Clone the project repository using Git or download the project ZIP file and extract it.
2.	Install Python 3 on your system if it is not already installed. You can download it from the official website.
3.	Navigate to the project directory using the command prompt or terminal.
4.	Create a virtual environment for the project to isolate it from your system's global Python environment. Enter the following command: python -m venv env
5.	Activate the virtual environment. Enter the following command: source env/bin/activate (Linux/MacOS) or env\Scripts\activate (Windows)
6.	Install the required project dependencies by running the following command: pip install -r requirements.txt
7.	Create a new SQLite database by running the following command: python manage.py migrate
8.	Create a superuser for the Django admin panel by running the following command: python manage.py createsuperuser
9.	Start the development server by running the following command: python manage.py runserver
Note that Django is included in the requirements.txt file, so you do not need to separately install it. The pip install -r requirements.txt command will install all necessary dependencies, including Django and Pillow.

Website: http://hozaifa1.pythonanywhere.com/

A more detailed description of the syntax used is on the documentation.txt file
