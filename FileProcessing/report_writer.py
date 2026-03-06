from datetime import datetime

from transformer import aggregate_by_store, aggregate_by_product


def write_summary_report(filepath, valid_records, errors, aggregations):
    """
    Write a formatted summary report.
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    print('=== Sales Processing Report ===')
    time = datetime.now()
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"{formatted_time}\n")
    print("Processing Statistics:")

    valid_records_processed = len(valid_records)
    errors_processed = len(errors)
    total_records_processed = valid_records_processed + errors_processed
    print(f"Total records: {total_records_processed}")
    print(f"Valid records: {valid_records_processed}")
    print(f"Error records: {errors_processed}")

    print("Errors:")
    for error in errors:
        print(error)

    print("Sales by Store:")
    sales_by_store = aggregate_by_store(valid_records)
    for key, value in sales_by_store.items():
        print(f"- {key}: {value:.2f}")

    print("Top Products:")
    top_products = aggregate_by_product(valid_records)
    sorted_top_products = dict(sorted(top_products.items(), key=lambda item: item[1], reverse=True))
    count = 1
    for key, value in sorted_top_products.items():
        print(f"{count}. {key}: {value}")
        count += 1

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    pass


def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    pass