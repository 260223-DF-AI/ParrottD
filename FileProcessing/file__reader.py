from exceptions import FileProcessingError
import os

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files

    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """

    records = []
    try:
        with open(filepath, 'r') as f:
            if f.read(1):
                return records

    except FileNotFoundError:
        raise FileProcessingError()


    for i, line in enumerate(f):
        if i == 0:
            continue
        entry = line.split(',')[:1]
        records.append({
            'date': entry[0],
            'store_id': entry[1],
            'product': entry[2],
            'quantity': entry[3],
            'price': entry[4],
        })
    return records