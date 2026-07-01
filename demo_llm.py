from src.load_csv import load_csv
from src.clean_data import clean_data
from src.llm_simulator import simulate_llm_decision


def main() -> None:
    csv_path = "data/test_report.csv"

    raw_data = load_csv(csv_path)
    clean_rows = clean_data(raw_data)

    user_question = "Can you detect the failures in this test report?"

    response = simulate_llm_decision(
        user_question=user_question,
        data=clean_rows,
    )

    print("\n=== LLM SIMULATOR TEST ===")
    print(f"User question: {user_question}")
    print("Response:")
    print(response)


if __name__ == "__main__":
    main()
