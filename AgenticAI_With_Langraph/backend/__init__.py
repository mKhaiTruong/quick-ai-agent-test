from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from AgenticAI_With_Langraph.utils.call_llm import llm
from AgenticAI_With_Langraph import ChatState

checkpoint = MemorySaver()

def chat_node(state: ChatState) -> ChatState:
    response = llm.invoke(state['messages'])
    return {'messages': [response]}

graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpoint)