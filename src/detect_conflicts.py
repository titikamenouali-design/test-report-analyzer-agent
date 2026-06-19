def detect_conflicts(df):
    """
    Detect critical conflicts and requirements with multiple results.
    """

    critical_conflicts = {}
    requirements_with_multiple_results = {}

    # 1. Critical conflicts:
    # Same requirement + same test_id with different results
    if "test_id" in df.columns:
        grouped_by_test = df.groupby(["requirement", "test_id"])["result"].unique()

        for (requirement, test_id), results in grouped_by_test.items():
            unique_results = list(results)

            if len(unique_results) > 1:
                key = f"{requirement} / {test_id}"
                critical_conflicts[key] = unique_results

    # 2. Requirement with multiple results:
    # Same requirement with different results across different test cases
    grouped_by_requirement = df.groupby("requirement")["result"].unique()

    for requirement, results in grouped_by_requirement.items():
        unique_results = list(results)

        if len(unique_results) > 1:
            requirements_with_multiple_results[requirement] = unique_results

    return {
        "critical_conflicts_count": len(critical_conflicts),
        "critical_conflicts": critical_conflicts,
        "requirements_with_multiple_results_count": len(requirements_with_multiple_results),
        "requirements_with_multiple_results": requirements_with_multiple_results
    }
