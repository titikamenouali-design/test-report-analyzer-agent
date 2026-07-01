from src.agent_context import AgentContext
from src.tool_router import execute_tool


def main() -> None:
    csv_path = "data/sample_test_results.csv"

    context = AgentContext(csv_path)
    context.load_data()

    response = execute_tool(
        "detect_failures_context",
        context=context,
    )

    print("\n=== CONTEXT TOOL TEST ===")
    print(response)


if __name__ == "__main__":
    main()
