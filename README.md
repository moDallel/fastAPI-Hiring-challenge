# FastAPI User Management API

This project is a simple API built with FastAPI that allows for the management of users. It provides endpoints for creating, updating, deleting, and retrieving user information.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
    - [Linux](#linux)
    - [Windows PowerShell](#windows-powershell)
  - [Installing Dependencies](#installing-dependencies)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Running the Application](#running-the-application)
- [Testing](#testing)

## Prerequisites

Before getting started, ensure you have the following prerequisites installed:

- Python 3.10 or higher

## Getting Started

To get started with this project, make sure you have Python 3.10 or higher installed on your system. If not, please install it before proceeding.

### Setting Up a Virtual Environment

#### Linux:

1. Create a new directory for your project:

    ```bash
    mkdir fastapi-challenge
    cd fastapi-challenge
    ```

2. Install `virtualenv` if you haven't already:

    ```bash
    pip install virtualenv
    ```

3. Create a virtual environment:

    ```bash
    virtualenv env_name
    ```

4. Activate the virtual environment:

    ```bash
    source env_name/bin/activate
    ```

#### Windows PowerShell:

1. Create a new directory for your project:

    ```bash
    mkdir fastapi-challenge
    cd fastapi-challenge
    ```

2. Create a virtual environment using `python -m venv`:

    ```powershell
    python -m venv .\env_name
    ```

3. Activate the virtual environment:

    ```powershell
    .\env_name\Scripts\Activate
    ```
### Clone the project
Clone this repository to your local machine:

```bash
git clone https://github.com/moDallel/fastAPI-Hiring-challenge.git
```

### Installing Dependencies

Once you have activated the virtual environment, install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

## Project Structure

The project follows a modular directory structure to organize its codebase:

```
project_name/
│
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   ├── models/
│   ├── db/
│   │   ├── __init__.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   └── schemas.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── useful_functions.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_endpoints/
│       └── test_user.py
├── README.md
├── requirements.txt
└── .gitignore
```

- `app/`: Contains the main application code.
- `app/api/`: Contains API-related code.
- `app/db/`: Contains database-related code.
-  `app/utils/`: Contains helpers functions.
- `tests/`: Contains test code.
- `README.md`: Project documentation.
- `requirements.txt`: List of project dependencies.
- `.gitignore`: Git ignore file.

## API Endpoints

The API provides the following endpoints:

- `POST /create_user/`: Create a new user.
- `GET /users/{email}`: Retrieve user information by email.
- `PUT /update_user/{email}`: Update user information by email.
- `DELETE /delete_user/{email}`: Delete user by email.
- `GET /users/`: Retrieve a list of all users.

## Dependencies

The project uses the following dependencies:

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- SQLite: Relational database management system.

## Running the Application

To run the application, execute the following command:

```bash
uvicorn app.main:app --reload --port <port>
```
The API will be accessible at http://localhost:8000 by default if you don't precise the port.

## Testing
- JUnit test are not developed for the moment
- Automated tests are included in the tests/ directory. You can run the tests using the following command:

```bash
pytest
```



