def calculate_statistics(df):
    """
    Calculate test campaign statistics from a cleaned DataFrame.
    Expected column:
    - Result
    """

    total_requirements = len(df)

    pass_count = (df["Result"] == "PASS").sum()
    fail_count = (df["Result"] == "FAIL").sum()

    executed_count = pass_count + fail_count
    not_executed_count = total_requirements - executed_count

    if executed_count > 0:
        pass_rate = round((pass_count / executed_count) * 100, 2)
    else:
        pass_rate = 0

    statistics = {
        "total_requirements": total_requirements,
        "executed_count": executed_count,
        "not_executed_count": not_executed_count,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_rate": pass_rate
    }

    return statistics
