def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    new_records = []
    total = 0
    for record in records:
        total += record['quantity'] * record['price']
        record.update({'total': total})
    return records
    pass

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    list_dicts = []
    for record in records:
        if record['store_id'] not in list_dicts:
            list_dicts.append({'store_id': record['store_id', 'total_sales': 0]})
        else:
            list_dicts[record['store_id']]['total'] += record['total']
    return list_dicts
    pass

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    list_dicts = []
    for record in records:
        if record['store_id'] not in list_dicts:
            list_dicts.append({'store_id': record['store_id', 'total_sales': 0]})
        else:
            list_dicts[record['store_id']]['quantity'] += record['quantity']
    return list_dicts
    pass