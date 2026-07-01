from src.tool_router import execute_tool


def simulate_llm_decision(user_question: str, data: list[dict]) -> dict:
    """
    Simulates an LLM choosing the appropriate tool based on a user question.

    This temporary function will later be replaced by a real LLM
    using Function Calling.
    """
    question = user_question.lower()

    if "failure" in question or "failures" in question or "failed" in question:
        return execute_tool("detect_failures", data=data)

    if "statistics" in question or "stats" in question or "summary" in question:
        return execute_tool("calculate_statistics", data=data)

    if "report" in question:
        statistics = execute_tool("calculate_statistics", data=data)
        failures = execute_tool("detect_failures", data=data)

        return execute_tool(
            "generate_report",
            statistics=statistics,
            failures=failures,
            missing_results=[],
            conflicts=[],
        )

    return {
        "error": True,
        "message": "No suitable tool found for this question.",
        "available_intents": [
            "detect_failures",
            "calculate_statistics",
            "generate_report",
        ],
    }
