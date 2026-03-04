from datetime import datetime

from exceptions import InvalidDataError, FileProcessingError, MissingFieldError


def validate_sales_record(record, line_number):
    """
    Validate a single sales record.
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number

    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    if any(value is None for value in record.values()):
        raise MissingFieldError("Missing required field ")
    try:
        # Try to parse the string into a datetime object using the specified format
        datetime.strptime(record["date"], "%Y-%m-%d")
    except FileProcessingError:
        raise InvalidDataError(f"- Line {line_number}: Invalid date format 'invalid-date'")


    if not isinstance(record["quantity"], int):
        raise InvalidDataError(f"- Line {line_number}: Invalid quantity {record['quantity']}")

    try:
        if record["quantity"] >= 1:
            test = 0
    except FileProcessingError:
        raise InvalidDataError(f"- Line {line_number}: Quantity must be positive, got {record['quantity']}")

    try:
        if record["price"] >= 1:
            float(record["price"])
    except FileProcessingError:
        raise InvalidDataError(f"- Line {line_number}: Invalid Price {record['price']}")

    return record


def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.

    Returns: Tuple of (valid_records, error_list)
    """
    valid_records = []
    len(records)
    valid_records = []
    error_list = []
    for index,record in enumerate(records):
        try:
            valid_record = validate_sales_record(record, index+1)
            valid_records.append(valid_record)
        except Exception as e:
            error_list.append(e)
    return (valid_records, error_list)