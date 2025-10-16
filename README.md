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

## Usage

1. **Register**: Create a new account with username and password
2. **Login**: Access your personal dashboard
3. **Add Todos**: Create new tasks with titles and descriptions
4. **Manage**: View, edit, or delete your todos
5. **Logout**: Secure session termination

## Key Features Demonstrated

- **Authentication System**: Complete user registration/login flow
- **Database Operations**: CRUD operations with SQLAlchemy ORM
- **Session Security**: Flask-Login integration with bcrypt hashing
- **Template Inheritance**: Modular HTML templates using Jinja2
- **Form Handling**: Secure form processing and validation

## Dependencies

All dependencies are listed in `requirements.txt`

## Installation & Setup

### Prerequisites
- Python 3.7+ installed on your system
- Git installed

### Steps

1. **Clone the repository:**
git clone https://github.com/sachin-paranjape/flask-todo-app.git
cd flask-todo-app

2. **Create virtual environment:**
virtualenv todo-env


3. **Activate virtual environment:**
**Windows (Command Prompt):**
todo-env\Scripts\activate

**Windows (PowerShell):**
todo-env\Scripts\Activate.ps1

**Linux/Mac:**
source todo-env/bin/activate

4. **Install dependencies:**
pip install -r requirements.txt

5. **Run the application:**
python app.py

6. **Open your browser and navigate to:**
http://localhost:8000/


### Deactivate Environment
When you're done, deactivate the virtual environment:



## Project Structure

flask-todo-app/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
│ ├── base.html # Base template with navbar
│ ├── index.html # Home page
│ ├── login.html # User login form
│ ├── register.html # User registration
│ ├── show.html # Display todos
│ ├── add.html # Add new todo
│ └── update.html # Edit existing todo
├── todo-env/ # Virtual environment (auto-generated)
└── instance/
└── todo.db # SQLite database (auto-generated)

