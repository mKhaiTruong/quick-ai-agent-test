import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from AgenticAI_With_Langraph.backend import chatbot
from AgenticAI_With_Langraph.helpers.session import get_config


def stream_response(user_input):
    return st.write_stream(
        chunk.content for chunk, _ in chatbot.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config      = get_config(),
            stream_mode = "messages"
        )
        if isinstance(chunk, AIMessage)
    )