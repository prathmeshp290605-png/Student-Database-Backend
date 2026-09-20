# Vector Database Research & Selection

## 1. Introduction

A vector database is used to store and search information using numerical vector embeddings. It is useful for semantic search and AI-based applications.

For this project, a vector database is required to allow the AI chatbot to retrieve relevant student information.

## 2. Vector Databases Considered

### ChromaDB

ChromaDB is an open-source vector database designed for AI and machine learning applications.

Advantages:
- Easy Python integration
- Simple local setup
- Supports embeddings and semantic search
- Suitable for small and medium-sized applications
- Easy to integrate with AI chatbot systems

### FAISS

FAISS (Facebook AI Similarity Search) is a library for efficient similarity search of vectors.

Advantages:
- Fast similarity search
- Developed for large-scale vector search
- Supports multiple indexing methods

Limitation:
- Requires additional database/storage management for a complete application.

### Pinecone

Pinecone is a managed cloud vector database.

Advantages:
- Cloud-based
- Scalable
- Designed for production AI applications

Limitation:
- Requires external cloud service and configuration.

## 3. Selected Vector Database

ChromaDB was selected for this project.

The main reasons are:

- Easy integration with Python
- Simple local development
- Supports semantic search
- Suitable for the student database chatbot
- Can work with embedding models
- Easy integration with the LangGraph-based chatbot

## 4. Usage in This Project

Student information is converted into documents and stored in ChromaDB.

When a user asks a question:

```text
User Question
      ↓
LangGraph
      ↓
ChromaDB Semantic Search
      ↓
Relevant Student Information
      ↓
Gemini API
      ↓
Final AI Response