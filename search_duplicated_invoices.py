

def create_invoices_pairs(all_invoices):
    duplicate_invoices = [] 

    for i in range(len(all_invoices) - 1):
        for j in range(i + 1, len(all_invoices)):
            if all_invoices[i]['gross amount'] == all_invoices[j]['gross amount']:
                duplicate_invoices.append([i, j])
    return duplicate_invoices


def find_matching_invoices(
    all_invoices,
    same_amount_invoices,
    column_name
):
    matched_pair = []
    for invoices_pair in same_amount_invoices:
        if all_invoices[invoices_pair[0]][column_name] == \
        all_invoices[invoices_pair[1]][column_name]:
            matched_pair.append(invoices_pair) 
    return matched_pair


def find_duplicated_invoices(same_amount_date, same_amount_reference):
    duplicated_pairs = []
    i = 0
    while i < len(same_amount_reference):
        if same_amount_reference[i] in same_amount_date:
            temp_pair = same_amount_reference.pop(i)
            duplicated_pairs.append(temp_pair)
            same_amount_date.remove(temp_pair)
        else: 
            i += 1
    return duplicated_pairs, same_amount_date, same_amount_reference


def eliminate_repeated_invoices(matched_invoices):
    for key, value in matched_invoices.items():
        temp = []
        for pair in value:
            if not temp:
                temp.append(set(pair))
                continue
            matched_rows = set(temp[-1]).intersection(set(pair))
            if len(matched_rows) > 0:
                temp[-1] |= set(pair)
            else:
                temp.append(set(pair))
        matched_invoices[key] = temp
    return matched_invoices


def execute(all_invoices):
    matched_invoices = {}
    matched_amounts = create_invoices_pairs(all_invoices)
    matched_invoices['amounts_dates_matched_'] = find_matching_invoices(
        all_invoices,
        matched_amounts,
        'document date' 
    )
    matched_invoices['amounts_references_matched_'] = find_matching_invoices(
        all_invoices,
        matched_amounts,
        'reference' 
    )
    (
        matched_invoices['duplicates_'],
        matched_invoices['amounts_dates_matched_'],
        matched_invoices['amounts_references_matched_']
    ) = find_duplicated_invoices(
        matched_invoices['amounts_dates_matched_'],
        matched_invoices['amounts_references_matched_']
    )
    matched_invoices = eliminate_repeated_invoices(matched_invoices)
    return matched_invoices
