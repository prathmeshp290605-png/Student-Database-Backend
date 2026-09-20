from fastapi import APIRouter

from schemas.chat import ChatRequest, ChatResponse
from chatbot.chatbot_graph import chatbot_graph


router = APIRouter(
    prefix="/chat",
    tags=["Chatbot"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = chatbot_graph.invoke({
        "message": request.message,
        "response": ""
    })

    return {
        "response": result["response"]
    }