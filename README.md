# Student CRUD API

## 1. Project Description

The Student CRUD API is a simple REST API developed using Python and FastAPI. It uses SQLModel to connect and interact with an SQLite database.

This project allows users to create, view, update, and delete student records. It also provides an API to get individual student details using their ID.

## 2. Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn

## 3. Project Structure

```text
student-crud/
│
├── app/
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

- **db.py:** Handles SQLite database connection, engine creation, and database sessions.
- **main.py:** Creates the FastAPI application, initializes the database, and includes the API router.
- **models.py:** Defines the Student table and the data models for creating and updating students.
- **routers.py:** Contains all student CRUD API endpoints.
- **students.db:** SQLite database file used to store student records.
- **requirements.txt:** Contains the required Python packages.
- **.gitignore:** Specifies files and folders that should not be tracked by Git.

## 4. Features

- Create a new student.
- View all students.
- View a single student using student ID.
- Update student information.
- Delete a student using student ID.
- SQLite database connectivity.
- Automatic database table creation.
- Error handling for students that do not exist.

## 5. Installation and Setup

### Step 1: Clone the Repository


git clone <your-repository-url>


### Step 2: Navigate to the Project Folder


cd student-crud


### Step 3: Create a Virtual Environment


python -m venv venv


### Step 4: Activate the Virtual Environment

For Windows:


venv\Scripts\activate


### Step 5: Install Required Packages


pip install -r requirements.txt


## 6. Run the Application

Run the following command from the main project folder:


uvicorn app.main:app --reload


The application will run at:

http://127.0.0.1:8000

## 7. API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open the following URL in your browser:

http://127.0.0.1:8000/docs

You can test all the CRUD operations directly from Swagger UI.

## 8. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Create a new student |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| PATCH | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## 9. Sample Requests

### Create Student

**POST** `/students`

Request Body:

json
{
    "name": "Asmita Pandeya",
    "email": "asmita@example.com"
}


### Update Student

**PATCH** `/students/1`

Request Body:

json
{
    "name": "Asmita Updated"
}


## 10. Database

This project uses SQLite as its database.

The database file is named `students.db`. The Student table is created automatically when the application starts.

The Student table contains the following fields:

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | String | Student name |
| email | String | Student email |
| can_login | Boolean | Login permission (default: True) |

## 11. Conclusion

This project helped me understand how to build REST APIs using FastAPI, connect an SQLite database using SQLModel, manage database sessions, and perform CRUD operations. It also helped me understand how to organize a FastAPI project into separate files and folders.