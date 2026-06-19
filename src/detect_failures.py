def detect_failures(df):
    """
    Detect failed requirements.
    """

    failed_df = df[df["result"] == "FAIL"]

    failed_requirements = failed_df["requirement"].tolist()

    return {
        "count": len(failed_requirements),
        "failed_requirements": failed_requirements
    }
