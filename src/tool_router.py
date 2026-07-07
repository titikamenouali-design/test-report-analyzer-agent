from src.tools import (
    detect_failures_tool,
    calculate_statistics_tool,
    generate_report_tool,
    detect_failures_context_tool,
    calculate_statistics_context_tool,
)


AVAILABLE_TOOLS = {
    "detect_failures": detect_failures_tool,
    "detect_failures_context": detect_failures_context_tool,
    "calculate_statistics": calculate_statistics_tool,
    "generate_report": generate_report_tool,
    "calculate_statistics_context": calculate_statistics_context_tool,
}


def execute_tool(tool_name, **kwargs):

    if tool_name not in AVAILABLE_TOOLS:
        return {
            "status": "error",
            "message": f"Unknown tool: {tool_name}",
            "available_tools": list(AVAILABLE_TOOLS.keys())
        }

    return AVAILABLE_TOOLS[tool_name](**kwargs)
