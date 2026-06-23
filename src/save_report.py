import json
from datetime import datetime
from pathlib import Path


def save_report(report, output_dir="outputs"):
    """
    Save the report as a timestamped JSON file.
    """

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = Path(output_dir) / f"report_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    return str(file_path)
