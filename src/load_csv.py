import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file and return a pandas DataFrame.
    """

    try:
        df = pd.read_csv(file_path)

        print(f"CSV loaded successfully")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")

        return df

    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None
