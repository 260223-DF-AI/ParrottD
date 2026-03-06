from file__reader import read_csv_file
from report_writer import write_summary_report
from transformer import calculate_totals, aggregate_by_store
from validator import validate_all_records


def process_sales_file(input_path, output_dir):
    """
    Main processing pipeline.

    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully

    Returns: ProcessingResult with statistics
    """
    print("Reading input file...")
    list_of_total_records = read_csv_file(input_path)
    valid_and_invalidrecords = validate_all_records(list_of_total_records)
    print(f"Test {valid_and_invalidrecords}")
    records_withsales = calculate_totals(valid_and_invalidrecords[0])
    store_total_sales = aggregate_by_store(records_withsales)
    write_summary_report(output_dir, valid_and_invalidrecords[0], valid_and_invalidrecords[1], store_total_sales)
    pass

def main():
    process_sales_file("sample_sales.csv", "log_data")

if __name__ == "__main__":
    # Process from command line
    main()
    pass