from langgraph.graph import StateGraph, START, END

from chatbot.chatbot_state import ChatState
from services.gemini_service import generate_response
from chatbot.student_tools import get_all_students


def chatbot_node(state: ChatState):

    user_message = state["message"]

    students = get_all_students()

    prompt = f"""
You are a Student Database AI Assistant.

You can answer questions about students using the database information below.

Student Database:
{students}

User Question:
{user_message}

Instructions:
- Answer clearly and concisely.
- Use only the student database information provided.
- If the requested information is not available, say that it was not found.
"""

    response = generate_response(prompt)

    return {
        "response": response
    }


graph_builder = StateGraph(ChatState)

graph_builder.add_node("chatbot", chatbot_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

chatbot_graph = graph_builder.compile()
