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
    }
]
