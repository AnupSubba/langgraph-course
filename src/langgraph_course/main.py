from httpcore import __name
from langgraph.constants import END
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph
from langgraph_course.nodes import run_agent_reasoning, tool_node

load_dotenv()

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1

def should_continue(state: MessagesState):
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT

flow = StateGraph(MessagesState)
flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(AGENT_REASON, should_continue, {
    END:END,
    ACT:ACT
})

flow.add_edge(ACT, AGENT_REASON)

workflow = flow.compile()

workflow.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__ == '__main__':
    print('Hello ReAct LangGraph with function Calling')
    res = workflow.invoke({"messages": [HumanMessage(content="What is the temperature of Delhi? List it and triple it")]})  
    print("messages: ", res["messages"][LAST].content) 