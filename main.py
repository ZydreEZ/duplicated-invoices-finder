import csv
import glob

# 1. read csv file

posted_invoices_list = [] # create empty list for all invoices from files. 

for file_name in glob.glob('./data/*.csv'): # glob method let to read all files from data folder. 
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";") 
        for row in reader: # read file rows as dictionaries
            posted_invoices_list.append(row) # add disctionaries to the list
# print(posted_invoices_list)

# 2. find duplicated invoices
# make file with matched amount and referenece and file with matched amount and document date. (suspected duplicate)
duplicate_invoices_list = [] # create empty list

# 2.1 search invoices with same amount

for invoice_1_index in range(len(posted_invoices_list) - 1):
    for invoice_2_index in range(invoice_1_index + 1, len(posted_invoices_list)):
        if posted_invoices_list[invoice_1_index]['gross amount'] == \
            posted_invoices_list[invoice_2_index]['gross amount']:
            duplicate_invoices_list.append([invoice_1_index, invoice_2_index])
# print(duplicate_invoices_list)
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
            matched_pair.append(invoices_pair) # add invoices which are with same values in column name from duplicate_invoices_list. 
    return matched_pair

matched_amounts_and_dates = find_matching_invoices(
    posted_invoices_list,
    duplicate_invoices_list,
    'document date' 
)
print(matched_amounts_and_dates)

matched_amounts_and_reference = find_matching_invoices(
    posted_invoices_list,
    duplicate_invoices_list,
    'reference' 
)
print(matched_amounts_and_reference)
def find_duplicated_invoices(same_amount_date, same_amount_reference):
    duplicated_pairs = []
    invoices_index = 0
    while invoices_index < len(same_amount_reference):
        if same_amount_reference[invoices_index] in same_amount_date:
            temp_pair_value = same_amount_reference.pop(invoices_index) #retur value and remove it from same amount ad reference list. 
            duplicated_pairs.append(temp_pair_value)
            same_amount_date.remove(temp_pair_value)
        invoices_index += 1
    return duplicated_pairs, same_amount_date, same_amount_reference


(
    duplicate_invoices_list,
    matched_amounts_and_dates,
    matched_amounts_and_reference
) = find_duplicated_invoices(
    matched_amounts_and_dates,
    matched_amounts_and_reference
)

print(duplicate_invoices_list)

# 2.3 search invoices with same reference number in updated duplicate_invoices_list
# eliminate full duplicates from partial duplicates lists.  

# duplicated_pair = 0
# while duplicated_pair < len(duplicate_invoices_list):
#     if posted_invoices_list[duplicate_invoices_list[duplicated_pair][0]]['reference'] != \
#        posted_invoices_list[duplicate_invoices_list[duplicated_pair][1]]['reference']:
#         duplicate_invoices_list.pop(duplicated_pair) #remove invoices which are with different date from duplicate_invoices_list. they are not duplicated invoices. 
#     duplicated_pair += 1
# print(duplicate_invoices_list)

# 3. TODO check if found duplicated invoice is not reversed by cheking clearing document number 

# 4. TODO save found duplicates in new file
# 5. After file with found duplicates cration, move Data files to archieved folder. 


# 6. TODO write function __main__