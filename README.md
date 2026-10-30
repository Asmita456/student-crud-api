# Student CRUD API

A simple RESTful API for managing student records, developed using **Python, FastAPI, SQLModel, SQLAlchemy, and SQLite**.

This project demonstrates how to build a backend application using FastAPI, connect to a relational database, and perform CRUD (Create, Read, Update, Delete) operations using SQLModel and SQLAlchemy.

## 1. Project Description

The Student CRUD API is a backend application developed using Python and FastAPI. It provides REST API endpoints to create, retrieve, update, and delete student records.

The application uses SQLModel and SQLAlchemy for database interaction and SQLite for storing student information.

It also provides automatic database table creation, database session management, request validation, and error handling.

## 2. Technologies Used

- **Python:** Programming language used to develop the application.
- **FastAPI:** Modern Python framework used to build REST APIs.
- **SQLModel:** ORM library used for database models, validation, and database operations.
- **SQLAlchemy:** SQL toolkit and ORM that powers the database operations through SQLModel.
- **SQLite:** Lightweight relational database used to store student records.
- **Uvicorn:** ASGI server used to run the FastAPI application.

## 3. Project Structure

```text
student-crud-api/
│
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   └── routers.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── students.db
```

### File Description

- **__init__.py:** Marks the `app` directory as a Python package, allowing its modules to be imported.
- **db.py:** Handles SQLite database connection, engine creation, database table creation, and database sessions.
- **main.py:** Creates the FastAPI application, initializes the database using the lifespan event, and includes the student API router.
- **models.py:** Defines the Student database table and data models for creating and updating student records.
- **routers.py:** Contains all student CRUD API endpoints and their database operations.
- **students.db:** SQLite database file used to store student records.
- **requirements.txt:** Contains the required Python packages.
- **README.md:** Provides project documentation, installation instructions, and API details.
- **.gitignore:** Specifies files and folders that should not be tracked by Git.

## 4. Features

- Create a new student record.
- Retrieve all student records.
- Retrieve an individual student using their ID.
- Update existing student information.
- Delete a student using their ID.
- SQLite database connectivity.
- SQLModel and SQLAlchemy integration.
- Automatic database table creation.
- Database session management.
- Request data validation.
- Error handling for students that do not exist.
- Interactive API documentation using Swagger UI.

## 5. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Asmita456/student-crud-api.git
```

### Step 2: Navigate to the Project Folder

```bash
cd student-crud-api
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**For Windows:**

```bash
venv\Scripts\activate
```

**For Linux/macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
fastapi
uvicorn
sqlmodel
```

SQLAlchemy is installed automatically as a dependency of SQLModel.

## 6. Run the Application

Run the following command from the main project directory:

```bash
uvicorn app.main:app --reload
```

The application will run at:

**Base URL:**

```text
http://127.0.0.1:8000
```

**Swagger UI:**

```text
http://127.0.0.1:8000/docs
```

**ReDoc:**

```text
http://127.0.0.1:8000/redoc
```

To stop the server, press `Ctrl + C`.

## 7. API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Through Swagger UI, users can:

- View all available API endpoints.
- Understand the required request parameters.
- Submit JSON request bodies.
- Execute CRUD operations.
- View API responses and HTTP status codes.

## 8. API Endpoints

The application provides the following API endpoints:

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Create a new student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PATCH | `/students/{student_id}` | Update student information |
| DELETE | `/students/{student_id}` | Delete a student by ID |

## 9. Sample API Requests

### 1. Create a Student

**Method:** POST

**Endpoint:** `/students`

Request Body:

```json
{
  "name": "Asmita Pandeya",
  "email": "asmita@example.com"
}
```

This endpoint creates a new student record in the database.

The student ID is generated automatically, and `can_login` defaults to `true`.

### 2. Get All Students

**Method:** GET

**Endpoint:** `/students`

No request body is required.

This endpoint retrieves all student records stored in the database.

Example Response:

```json
[
  {
    "id": 1,
    "name": "Asmita Pandeya",
    "email": "asmita@example.com",
    "can_login": true
  }
]
```

### 3. Get Student by ID

**Method:** GET

**Endpoint:** `/students/1`

No request body is required.

This endpoint retrieves the student whose ID is `1`.

### 4. Update Student Information

**Method:** PATCH

**Endpoint:** `/students/1`

Request Body:

```json
{
  "name": "Asmita Updated"
}
```

This endpoint updates only the specified student information.

You can also update the email and login permission:

```json
{
  "email": "updated@example.com",
  "can_login": false
}
```

The fields are optional, so you only need to provide the information you want to change.

### 5. Delete a Student

**Method:** DELETE

**Endpoint:** `/students/1`

No request body is required.

This endpoint deletes the student whose ID is `1` from the database.

Successful Response:

```json
{
  "message": "Student deleted successfully"
}
```

## 10. Database Structure

This project uses **SQLite** as its database and SQLModel with SQLAlchemy for database operations.

The database file is named `students.db`.

The Student table is created automatically when the application starts.

### Student Table

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Primary key and unique student identifier |
| name | String | Student's name |
| email | String | Student's email address |
| can_login | Boolean | Indicates whether the student is allowed to log in (default: True) |

### Database Operations

- **Database Engine:** Creates a connection between the application and SQLite.
- **Database Session:** Manages communication between API endpoints and the database.
- **SQLModel:** Defines database models and performs database operations.
- **SQLAlchemy:** Provides the underlying ORM and SQL database functionality.
- **SQLite:** Stores student records in the `students.db` file.

## 11. Error Handling

The API handles situations where a requested student does not exist.

For example, when a user tries to retrieve, update, or delete a student using an invalid ID, the API returns:

**HTTP Status Code:** `404 Not Found`

Example Response:

```json
{
  "detail": "Student not found"
}
```

FastAPI also provides automatic request validation and returns appropriate validation errors when invalid data is submitted.

## 12. Application Workflow

The application follows a structured workflow:

1. The user sends an HTTP request to a FastAPI endpoint.
2. FastAPI receives the request and validates the submitted data.
3. The router processes the requested CRUD operation.
4. A database session is provided through FastAPI dependency injection.
5. SQLModel and SQLAlchemy perform the required database operations.
6. SQLite stores or retrieves the student records.
7. The API returns the appropriate response to the user.

### Role of Each Application File

- `main.py` initializes the FastAPI application and database.
- `db.py` manages database connections and sessions.
- `models.py` defines the database and request models.
- `routers.py` handles API endpoints and CRUD operations.
- `__init__.py` identifies the application directory as a Python package.

## 13. Conclusion

This project helped me understand how to develop RESTful APIs using FastAPI, connect an SQLite database using SQLModel and SQLAlchemy, manage database sessions, and perform CRUD operations.

It also provided practical knowledge of API routing, request handling, data validation, database connectivity, error handling, and organizing a Python backend project into separate modules.

Overall, the Student CRUD API demonstrates the basic implementation of a backend application for managing student records using modern Python technologies.

## 14. Author

**Developed by:** Asmita Pandeya

**Project:** Student CRUD API

**Technologies:** Python, FastAPI, SQLModel, SQLAlchemy, SQLite, Uvicorn

---

*Developed as a learning project to understand REST API development and database integration using Python.*