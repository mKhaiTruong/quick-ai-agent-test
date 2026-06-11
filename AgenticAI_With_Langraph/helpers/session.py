import streamlit as st
import uuid
from langchain_core.messages import HumanMessage, AIMessage
from AgenticAI_With_Langraph.backend import chatbot

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)

def init_session():
    st.session_state.setdefault("message_history", [])
    st.session_state.setdefault("chat_threads", [])
    st.session_state.setdefault("thread_id", str(uuid.uuid4()))
    
    add_thread(st.session_state["thread_id"])

def get_config():
    return {"configurable": {"thread_id": st.session_state["thread_id"]}}

def load_conversation(thread_id):
    state = chatbot.get_state(
        config={"configurable": {"thread_id": thread_id}}
    )
    
    temp_messages = []
    for message in state.values.get("messages", []):
        if isinstance(message, HumanMessage):
            role = "user"
        elif isinstance(message, AIMessage):
            role = "assistant"
        else:
            continue
        temp_messages.append({"role": role, "content": message.content})
    
    return temp_messages