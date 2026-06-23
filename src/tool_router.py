from src.tools import (
    detect_failures_tool,
    calculate_statistics_tool,
    generate_report_tool
)


AVAILABLE_TOOLS = {
    "detect_failures": detect_failures_tool,
    "calculate_statistics": calculate_statistics_tool,
    "generate_report": generate_report_tool
}


def execute_tool(tool_name, **kwargs):
    """
    Execute a tool by name.
    """

    if tool_name not in AVAILABLE_TOOLS:
        raise ValueError(f"Unknown tool: {tool_name}")

    return AVAILABLE_TOOLS[tool_name](**kwargs)
