tools = [
    {
        "name": "detect_failures",
        "description": "Detect failed requirements from a CSV test report.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the CSV test report file."
                }
            },
            "required": ["file_path"]
        }
    },

    {
        "name": "generate_report",
        "description": "Generate and save a full JSON test campaign report from a CSV file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the CSV test report file."
                }
            },
            "required": ["file_path"]
    }
}
]
