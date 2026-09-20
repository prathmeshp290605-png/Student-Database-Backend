import streamlit as st
import requests

# Render FastAPI backend
API_URL = "https://student-database-backend-u4bb.onrender.com"

st.set_page_config(
    page_title="Student Database AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Database Application")
st.caption("FastAPI + Gemini + LangGraph + ChromaDB")

# -----------------------------
# SIDEBAR
# -----------------------------

menu = st.sidebar.radio(
    "Select Option",
    ["Students", "Add Student", "AI Chatbot"]
)

# -----------------------------
# STUDENTS
# -----------------------------

if menu == "Students":

    st.header("📚 Student Database")

    try:
        response = requests.get(
            f"{API_URL}/students/",
            timeout=30
        )

        if response.status_code == 200:
            students = response.json()

            if students:
                st.dataframe(
                    students,
                    use_container_width=True
                )
            else:
                st.info("No students found.")

        else:
            st.error("Unable to fetch students.")

    except Exception as e:
        st.error(f"Connection error: {e}")


# -----------------------------
# ADD STUDENT
# -----------------------------

elif menu == "Add Student":

    st.header("➕ Add New Student")

    with st.form("student_form"):

        name = st.text_input("Student Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=1, max_value=100)
        course = st.text_input("Course")
        year = st.number_input("Year", min_value=1, max_value=10)
        marks = st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0
        )

        submit = st.form_submit_button("Add Student")

        if submit:

            student_data = {
                "name": name,
                "email": email,
                "age": age,
                "course": course,
                "year": year,
                "marks": marks
            }

            try:

                response = requests.post(
                    f"{API_URL}/students/",
                    json=student_data,
                    timeout=30
                )

                if response.status_code == 200:
                    st.success(
                        "Student added successfully!"
                    )
                else:
                    st.error(
                        f"Error: {response.text}"
                    )

            except Exception as e:
                st.error(f"Connection error: {e}")


# -----------------------------
# AI CHATBOT
# -----------------------------

elif menu == "AI Chatbot":

    st.header("🤖 Student AI Chatbot")

    question = st.text_input(
        "Ask something about a student"
    )

    if st.button("Ask AI"):

        if question.strip():

            try:

                response = requests.post(
                    f"{API_URL}/chat/",
                    json={
                        "message": question
                    },
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        result["response"]
                    )

                else:
                    st.error(
                        f"Chatbot error: {response.text}"
                    )

            except Exception as e:
                st.error(
                    f"Connection error: {e}"
                )

        else:
            st.warning("Please enter a question.")