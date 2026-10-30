
from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    can_login: bool = True


class StudentCreate(SQLModel):
    name: str
    email: str


class StudentUpdate(SQLModel):
    name: str | None = None
    email: str | None = None
    can_login: bool | None = None
