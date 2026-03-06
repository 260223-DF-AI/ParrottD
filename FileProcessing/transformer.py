def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    new_records = []
    total = 0
    for record in records:
        total = record['quantity'] * record['price']
        record.update({'total': total})
    return records
    pass

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    dict = {}
    for record in records:
        if record['store_id'] not in dict:
            if record['store_id']:
                dict.update({record['store_id']: 0})
        if record['store_id']  in dict:
            current = dict.get(record['store_id'])
            dict.update({record['store_id']: current + record['total']})
    return dict
    pass

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    dict = {}
    for record in records:
        if record['product'] not in dict:
            dict.update({record['product']: 0})
        if record['product'] in dict:
            current = dict.get(record['product'])
            dict.update({record['product']: current + record['quantity']})
    return dict
    pass