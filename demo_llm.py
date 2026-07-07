def main() -> None:
    csv_path = "data/sample_test_results.csv"

    context = AgentContext(csv_path)
    context.load_data()

    response = execute_tool(
        "detect_failures_context",
        context=context,
    )

    print("\n=== DETECT FAILURES TEST ===")
    print(response)

    statistics_response = execute_tool(
        "calculate_statistics_context",
        context=context,
    )

    print("\n=== CALCULATE STATISTICS TEST ===")
    print(statistics_response)


if __name__ == "__main__":
    main()
