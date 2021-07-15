
# 2. find duplicated invoices
# make file with matched amount and referenece and file with matched amount and document date. (suspected duplicate)

def create_invoices_pairs(posted_invoices_list):
    duplicate_invoices_list = [] # create empty list

    # 2.1 search invoices with same amount

    for invoice_1_index in range(len(posted_invoices_list) - 1):
        for invoice_2_index in range(invoice_1_index + 1, len(posted_invoices_list)):
            if posted_invoices_list[invoice_1_index]['gross amount'] == \
                posted_invoices_list[invoice_2_index]['gross amount']:
                duplicate_invoices_list.append([invoice_1_index, invoice_2_index])
    return duplicate_invoices_list

# 2.2 search invoices with same document date in duplicate_invoices_list

def find_matching_invoices(
    posted_invoices_list,
    duplicate_list,
    column_name
):
    matched_pair = []
    for invoices_pair in duplicate_list:
        if posted_invoices_list[invoices_pair[0]][column_name] == \
        posted_invoices_list[invoices_pair[1]][column_name]:
            matched_pair.append(invoices_pair) # add invoices which are with same values in column.
    return matched_pair


def find_duplicated_invoices(same_amount_date, same_amount_reference):
    duplicated_pairs = []
    invoices_index = 0
    while invoices_index < len(same_amount_reference):
        if same_amount_reference[invoices_index] in same_amount_date:
            temp_pair_value = same_amount_reference.pop(invoices_index) #return value and remove it from same amount and reference list. 
            duplicated_pairs.append(temp_pair_value)
            same_amount_date.remove(temp_pair_value)
        else: 
            invoices_index += 1
    return duplicated_pairs, same_amount_date, same_amount_reference


def execute(posted_invoices_list):
    matched_invoices = {}
    matched_amounts = create_invoices_pairs(posted_invoices_list)
    matched_invoices['amounts_dates_matched_'] = find_matching_invoices(
        posted_invoices_list,
        matched_amounts,
        'document date' 
    )

    matched_invoices['amounts_references_matched_'] = find_matching_invoices(
        posted_invoices_list,
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
    return matched_invoices
