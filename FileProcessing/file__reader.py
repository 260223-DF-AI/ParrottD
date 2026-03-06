from exceptions import FileProcessingError
import os
import os

def is_file_empty(file_path):
    """Check if a file is empty by its size."""
    # This will raise a FileNotFoundError if the file doesn't exist
    return os.path.getsize(file_path) == 0

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
             f.read()
             f.close()

    except FileNotFoundError:
        raise FileProcessingError()
    if is_file_empty(filepath):
        return records
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            entry = line.split(",")[::1]
            records.append({
                'date': entry[0],
                'store_id': entry[1],
                'product': entry[2],
                'quantity': entry[3],
                'price': entry[4],
            })
    return records