# Student Database Application System – Backend

A modular backend application for managing student data using FastAPI, SQLite, SQLAlchemy, Gemini API, LangGraph, and ChromaDB.

## Features

- Student CRUD operations
- FastAPI REST APIs
- Swagger API documentation
- SQLite database
- SQLAlchemy ORM
- Gemini API integration
- AI chatbot using LangGraph
- Student database interaction through chatbot
- ChromaDB vector database
- Semantic student data search
- Modular backend architecture

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Google Gemini API
- LangGraph
- ChromaDB
- Pydantic

## Project Structure

```text
Student-Database-Backend/
│
├── chatbot/
│   ├── chatbot_state.py
│   ├── chatbot_graph.py
│   ├── student_tools.py
│   └── __init__.py
│
├── database/
│   └── connection.py
│
├── models/
│   └── student.py
│
├── schemas/
│   ├── student.py
│   └── chat.py
│
├── routers/
│   ├── student_router.py
│   └── chat_router.py
│
├── services/
│   ├── student_service.py
│   └── gemini_service.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md