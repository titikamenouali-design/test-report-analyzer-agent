from src.load_csv import load_csv
from src.clean_data import clean_data
from src.detect_failures import detect_failures
from src.statistics import calculate_statistics
from src.detect_missing_results import detect_missing_results
from src.detect_conflicts import detect_conflicts
from src.generate_report import generate_report
from src.save_report import save_report

def detect_failures_tool(file_path):
    """
    Tool wrapper for failure detection.
    """

    df = load_csv(file_path)
    df = clean_data(df)

    return detect_failures(df)

def calculate_statistics_tool(file_path):
    """
    Tool wrapper for test campaign statistics.
    """

    df = load_csv(file_path)
    df = clean_data(df)

    return calculate_statistics(df)

def generate_report_tool(file_path):
    """
    End-to-end tool wrapper to generate and save a full test report.
    """

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

    saved_file = save_report(report)

    return {
        "report": report,
        "saved_file": saved_file
    }
def detect_failures_context_tool(context):
    """
    Tool wrapper using an AgentContext instance.
    """
    return detect_failures(context.get_data())
    
def calculate_statistics_context_tool(context):
    """
    Tool wrapper using an AgentContext instance
    for statistics calculation.
    """

    return calculate_statistics(context.get_data())

def detect_missing_results_context_tool(context):
    return detect_missing_results(context.get_data())

def detect_conflicts_context_tool(context):
    return detect_conflicts(context.get_data())

def generate_report_context_tool(context):
    return generate_report(context.get_data())


