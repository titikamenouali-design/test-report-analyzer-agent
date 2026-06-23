from src.load_csv import load_csv
from src.clean_data import clean_data
from src.statistics import calculate_statistics
from src.detect_failures import detect_failures
from src.detect_missing_results import detect_missing_results
from src.detect_conflicts import detect_conflicts
from src.generate_report import generate_report
from src.save_report import save_report
from src.tool_router import execute_tool


file_path = "data/sample_test_results.csv"

df = load_csv(file_path)
df = clean_data(df)

statistics = calculate_statistics(df)
failures = detect_failures(df)
missing_results = detect_missing_results(df)
conflicts = detect_conflicts(df)

report = generate_report(
    statistics,
    failures,
    missing_results,
    conflicts
)

print("\n=== REPORT ===")
print(report)

print("=== STATISTICS ===")
print(statistics)

print("\n=== FAILURES ===")
print(failures)

print("\n=== MISSING RESULTS ===")
print(missing_results)

print("\n=== CONFLICTS ===")
print(conflicts)

report_path = save_report(report)

print("\n=== REPORT SAVED ===")
print(report_path)

print("\n=== TOOL ROUTER TEST ===")

result = execute_tool(
    "detect_failures",
    file_path="data/sample_test_results.csv"
)

print(result)
