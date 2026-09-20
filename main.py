from fastapi import FastAPI
from database.connection import Base, engine
from models.student import Student
from routers.student_router import router as student_router
from routers.chat_router import router as chat_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Database Application System",
    description="Backend API for Student Database Management",
    version="1.0.0"
)
app.include_router(student_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "Student Database Backend is running!"
    }