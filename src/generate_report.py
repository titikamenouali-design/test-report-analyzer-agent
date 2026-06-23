def generate_report(statistics, failures, missing_results, conflicts):
    """
    Generate a structured JSON-ready report.
    """

    report = {
        "executive_summary": {
            "total_valid_requirements": statistics["total_valid_requirements"],
            "executed_count": statistics["executed_count"],
            "not_executed_count": statistics["not_executed_count"],
            "missing_results_count": statistics["missing_results_count"],
            "pass_count": statistics["pass_count"],
            "fail_count": statistics["fail_count"],
            "pass_rate": statistics["pass_rate"]
        },
        "failures": failures,
        "missing_results": missing_results,
        "conflicts": conflicts
    }

    return report
