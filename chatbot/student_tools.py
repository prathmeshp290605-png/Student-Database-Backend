import chromadb

from database.connection import SessionLocal
from models.student import Student


# ChromaDB setup
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="students"
)


def get_all_students():
    db = SessionLocal()

    try:
        students = db.query(Student).all()

        print("DEBUG - Students from database:", len(students))

        return [
            {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "age": student.age,
                "course": student.course,
                "year": student.year,
                "marks": student.marks
            }
            for student in students
        ]

    finally:
        db.close()


def find_student_by_email(email: str):
    db = SessionLocal()

    try:
        student = (
            db.query(Student)
            .filter(Student.email == email)
            .first()
        )

        if not student:
            return {
                "message": "Student not found"
            }

        return {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "age": student.age,
            "course": student.course,
            "year": student.year,
            "marks": student.marks
        }

    finally:
        db.close()


def search_students_in_vector_db(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results["documents"][0]


def sync_students_to_vector_db():
    students = get_all_students()

    if not students:
        print("No students found in database.")
        return

    for student in students:
        document = (
            f"Student {student['name']} is studying "
            f"{student['course']} in year {student['year']}. "
            f"Their age is {student['age']} and marks are "
            f"{student['marks']}. Email: {student['email']}."
        )

        collection.upsert(
            documents=[document],
            ids=[f"student_{student['id']}"]
        )

    print(f"Synced {len(students)} student(s) to ChromaDB.")
