from sqlalchemy.orm import Session

from models.student import Student
from schemas.student import StudentCreate


def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        email=student.email,
        age=student.age,
        course=student.course,
        year=student.year,
        marks=student.marks
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student
def get_all_students(db: Session):
    return db.query(Student).all()
def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        return None

    db_student.name = student.name
    db_student.email = student.email
    db_student.age = student.age
    db_student.course = student.course
    db_student.year = student.year
    db_student.marks = student.marks

    db.commit()
    db.refresh(db_student)

    return db_student
def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        return None

    db.delete(db_student)
    db.commit()

    return db_student