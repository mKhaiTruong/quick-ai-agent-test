import streamlit as st
from AgenticAI_With_Langraph.backend import chatbot
from AgenticAI_With_Langraph.helpers.session import init_session
from AgenticAI_With_Langraph.helpers.streaming import stream_response
from AgenticAI_With_Langraph.components.sidebar import render_sidebar

# ── init ─────────────────────────────────────────────
init_session()

# ── sidebar ──────────────────────────────────────────
render_sidebar()

# ── main ─────────────────────────────────────────────
st.title("Agentic Chatbot with LangGraph")

for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

if user_input := st.chat_input("Type here"):
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        ai_message = stream_response(user_input)

    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})