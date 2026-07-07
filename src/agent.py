from src.llm_simulator import simulate_llm_decision
from src.tool_router import execute_tool


class Agent:
    """
    Simple agent orchestrator.

    Responsible for:
    - receiving user requests
    - asking the LLM simulator for a tool decision
    - executing the selected tool
    """

    def __init__(self, context):
        self.context = context

    def run(self, user_question: str):
        decision = simulate_llm_decision(user_question)

        if "error" in decision:
            return decision

        tool_name = decision["tool_name"]
        arguments = decision.get("arguments", {})

        return execute_tool(
            tool_name,
            context=self.context,
            **arguments
        )
