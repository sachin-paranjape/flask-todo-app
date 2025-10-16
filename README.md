# Flask Todo Application

A full-stack web application with user authentication and CRUD operations.

## Features
- User registration/login with Flask-Login
- Personal todo management
- Session-based authentication
- SQLite database integration

## Technologies Used
- **Backend**: Flask, SQLAlchemy, Flask-Login, Flask-Bcrypt
- **Frontend**: HTML5, CSS3, Jinja2 templates
- **Database**: SQLite

## Development Process
- Used ChatGPT for scaffolding UI components and authentication routes
- Applied LLM assistance for initial HTML templates and Flask route handlers
- Implemented human review and testing for security and functionality

## Installation
- git clone https://github.com/sachin-paranjape/flask-todo-app.git
- cd flask-todo-app
- virtualenv todo-env
- source todo-env/bin/activate # Windows (Command Prompt) : todo-env\Scripts\activate #Windows (Powershell) : todo-env\Scripts\Activate.ps1
- pip install -r requirements.txt
- python app.py