def detect_missing_results(df):
    """
    Detect requirements with missing results.
    """

    missing_df = df[df["result"] == "EMPTY"]

    missing_requirements = missing_df["requirement"].drop_duplicates().tolist()

    return {
        "count": len(missing_requirements),
        "missing_requirements": missing_requirements
    }
