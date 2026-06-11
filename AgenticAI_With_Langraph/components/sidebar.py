import streamlit as st
import uuid
from AgenticAI_With_Langraph.helpers.session import load_conversation


def render_sidebar():
    st.sidebar.title("My Convo")
    
    if st.sidebar.button("+ New Chat"):
        new_thread_id = str(uuid.uuid4())
        st.session_state["thread_id"] = new_thread_id
        st.session_state["chat_threads"].append(new_thread_id)
        st.session_state["message_history"] = []
        st.rerun()
    
    st.sidebar.divider()
    
    for thread_id in st.session_state.get("chat_threads", []):
        label = f"Chat {thread_id[:8]}..."
        if st.sidebar.button(label, key=thread_id):
            if st.session_state["thread_id"] != thread_id:
                st.session_state["thread_id"] = thread_id
                st.session_state["message_history"] = load_conversation(thread_id)
                st.rerun()