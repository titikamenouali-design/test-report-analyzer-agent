from src.load_csv import load_csv
from src.clean_data import clean_data


class AgentContext:
    """
    Stores shared data for the agent during a session.

    The CSV is loaded and cleaned once, then reused by tools.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_data(self) -> None:
        raw_data = load_csv(self.file_path)

        if raw_data is None:
            raise ValueError(f"Unable to load CSV file: {self.file_path}")

        self.data = clean_data(raw_data)

    def get_data(self):
        if self.data is None:
            raise ValueError("Data has not been loaded yet.")

        return self.data
