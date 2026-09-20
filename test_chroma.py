import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="students"
)

collection.add(
    documents=[
        "Prathmesh Patil is a Computer Science Engineering student.",
        "Prathmesh Patil has scored 85.5 marks."
    ],
    ids=[
        "student_1",
        "student_1_marks"
    ]
)

results = collection.query(
    query_texts=["What are Prathmesh Patil marks?"],
    n_results=2
)

print(results)