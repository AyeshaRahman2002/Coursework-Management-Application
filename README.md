# Coursework Management Application

## Overview

This is a web-based application designed to manage coursework tasks and assignments. It provides functionality for users to create, update, search, and mark tasks as completed or incomplete. The app uses a SQLite database for data persistence and features various templates for user interaction.

## Project Structure

The project has the following structure:

- **`app/`**: Contains the main application files.
  - **`models.py`**: Defines the database models.
  - **`views.py`**: Contains the application logic and routing.
  - **`forms.py`**: Defines the forms used in the app for user input.
  - **`templates/`**: Holds HTML files for rendering views.
  - **`static/`**: Stores static files like CSS.
  
- **`migrations/`**: Contains migration scripts for database management.

- **`config.py`**: Configuration file for the app.

- **`run.py`**: Main entry point to run the application.

## Installation

### Prerequisites

- Python 3.8+
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```bash
    python db_create.py
    ```

5. Run the application:

    ```bash
    python run.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Features

- **Task Creation**: Users can create tasks with details such as name, description, and due date.
- **Task Search**: Users can search for tasks by keywords.
- **Task Status Management**: Mark tasks as completed or incomplete.
- **Responsive UI**: The application has a simple, responsive user interface.

## Technologies

- **Python 3.8+**
- **Flask**: Lightweight web framework
- **SQLite**: Database for storing task data
- **HTML/CSS**: Frontend interface

## Database Migrations

The application uses Flask-Migrate for database migrations. To create a new migration:

```bash
flask db migrate -m "Migration message"
flask db upgrade
```

### This project is part of a coursework done at University of Leeds.
