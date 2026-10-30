
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import Student, StudentCreate, StudentUpdate

router = APIRouter()


@router.post("/students")
def create_student(
    data: StudentCreate,
    session: Session = Depends(get_session)
):
    student = Student.model_validate(data)

    session.add(student)
    session.commit()
    session.refresh(student)

    return student


@router.get("/students")
def get_students(session: Session = Depends(get_session)):
    return session.exec(select(Student)).all()


@router.get("/students/{student_id}")
def get_student(
    student_id: int,
    session: Session = Depends(get_session)
):
    student = session.get(Student, student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.patch("/students/{student_id}")
def update_student(
    student_id: int,
    data: StudentUpdate,
    session: Session = Depends(get_session)
):
    student = session.get(Student, student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.sqlmodel_update(data.model_dump(exclude_unset=True))

    session.add(student)
    session.commit()
    session.refresh(student)

    return student



@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    session: Session = Depends(get_session)
):
    student = session.get(Student, student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    session.delete(student)
    session.commit()

    return {"message": "Student deleted successfully"}
