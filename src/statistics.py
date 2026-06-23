def calculate_statistics(df):
    """
    Calculate test campaign statistics from a cleaned DataFrame.
    Expected normalized column:
    - result
    """

    valid_df = df[df["result"] != "EMPTY"]

    total_requirements = len(valid_df)

    pass_count = (valid_df["result"] == "PASS").sum()
    fail_count = (valid_df["result"] == "FAIL").sum()

    executed_count = pass_count + fail_count
    not_executed_count = total_requirements - executed_count

    missing_count = (df["result"] == "EMPTY").sum()

    if executed_count > 0:
        pass_rate = round((pass_count / executed_count) * 100, 2)
    else:
        pass_rate = 0

    return {
        "total_valid_requirements": int(total_requirements),
        "executed_count": int(executed_count),
        "not_executed_count": int(not_executed_count),
        "missing_results_count": int(missing_count),
        "pass_count": int(pass_count),
        "fail_count": int(fail_count),
        "pass_rate": float(pass_rate)
}
    