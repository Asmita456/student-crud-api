# Student CRUD API

A simple RESTful API for managing student records, built using **Python, FastAPI, SQLModel, and SQLite**.

This project allows users to create, retrieve, update, and delete student records through REST API endpoints. It uses SQLModel for database operations and SQLite for storing student information.

## 1. Project Description

The Student CRUD API is a backend application developed using FastAPI. It provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on student records.

The application connects to an SQLite database using SQLModel and automatically creates the required database tables when the application starts.

## 2. Technologies Used

| Technology | Description |
|---|---|
| Python | Programming language |
| FastAPI | Framework for building REST APIs |
| SQLModel | ORM for database operations and data validation |
| SQLite | Database for storing student records |
| Uvicorn | ASGI server for running the application |

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
- **db.py:** Handles SQLite database connection, engine creation, table creation, and database sessions.
- **main.py:** Creates the FastAPI application, initializes the database, and includes the student API router.
- **models.py:** Defines the Student database table and data models for creating and updating student records.
- **routers.py:** Contains all student CRUD API endpoints.
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
- Automatic database table creation.
- Database session management.
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

## 6. Run the Application

Run the following command from the main project directory:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

To stop the server, press `Ctrl + C`.

## 7. API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open the following URL in your browser:

**Swagger UI:**

```text
http://127.0.0.1:8000/docs
```

**ReDoc:**

```text
http://127.0.0.1:8000/redoc
```

You can test all CRUD operations directly through Swagger UI without using any additional API testing tool.

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

### 2. Get All Students

**Method:** GET

**Endpoint:** `/students`

No request body is required.

This endpoint retrieves all student records from the database.

### 3. Get Student by ID

**Method:** GET

**Endpoint:** `/students/1`

No request body is required.

This endpoint retrieves the student whose ID is 1.

### 4. Update Student Information

**Method:** PATCH

**Endpoint:** `/students/1`

Request Body:

```json
{
  "name": "Asmita Updated"
}
```

Only the fields that need to be changed should be included in the request body.

You can also update the email and login permission:

```json
{
  "email": "updated@example.com",
  "can_login": false
}
```

### 5. Delete a Student

**Method:** DELETE

**Endpoint:** `/students/1`

No request body is required.

This endpoint deletes the student whose ID is 1 from the database.

## 10. Database Structure

This project uses **SQLite** as its database. The database file is named `students.db`.

The Student table is created automatically when the application starts.

### Student Table

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Primary key and unique student identifier |
| name | String | Student's name |
| email | String | Student's email address |
| can_login | Boolean | Indicates whether the student is allowed to log in (default: True) |

### Database Operations

The database operations are managed using SQLModel.

- Database engine establishes the connection with SQLite.
- Database sessions handle communication between the API and database.
- SQLModel manages database records and queries.
- FastAPI dependency injection provides database sessions to API endpoints.

## 11. Error Handling

The API handles situations where a requested student does not exist.

For example, when a user tries to retrieve, update, or delete a student with an invalid ID, the API returns:

**HTTP Status Code:** `404 Not Found`

Example Response:

```json
{
  "detail": "Student not found"
}
```

FastAPI also provides automatic request validation and returns appropriate validation errors when invalid data is submitted.

## 12. Conclusion

This project helped me understand how to develop RESTful APIs using FastAPI, connect an SQLite database using SQLModel, manage database sessions, and perform CRUD operations.

It also provided practical knowledge of API routing, request handling, data validation, error handling, and organizing a Python backend project into separate modules.

Overall, the Student CRUD API demonstrates the basic implementation of a backend application for managing student records using modern Python technologies.

---
## 13. Author

Developed by: Asmita Pandeya

Project: Student CRUD API