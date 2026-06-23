from src.load_csv import load_csv
from src.clean_data import clean_data
from src.detect_failures import detect_failures


def detect_failures_tool(file_path):
    """
    Tool wrapper for failure detection.
    """

    df = load_csv(file_path)
    df = clean_data(df)

    return detect_failures(df)
