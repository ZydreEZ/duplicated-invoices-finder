import csv
import glob
from datetime import datetime


def read_files(input_folder):
    all_invoices = []  

    for file_name in glob.glob(input_folder + '/*.csv'):
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";") 
            for row in reader: 
                all_invoices.append(row) 
    return all_invoices


def write_to_file(all_invoices, matched_invoices, user_choises):
    name_variations = get_files_variations(user_choises['result_type'])
    header = list(all_invoices[0].keys())
    empty_row = {}
    for key in header:
        empty_row[key] = None
    for variation in name_variations:
        if user_choises['out_file']:
            file_name = variation + user_choises['out_file']
        else:
            file_name = variation + datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(user_choises['out_dir'] + '/' + file_name + '.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, delimiter=";", fieldnames=header)
            writer.writeheader()
            for pair in matched_invoices[variation]:
                for ele in pair:
                    writer.writerow(all_invoices[ele])  
                writer.writerow(empty_row)


def get_files_variations(result_type):
    variations = {
        "1": ['duplicates_', 'amounts_references_matched_', 'amounts_dates_matched_'],
        "2": ['duplicates_', 'amounts_references_matched_'],
        "3": ['duplicates_', 'amounts_dates_matched_'],
        "4": ['amounts_references_matched_', 'amounts_dates_matched_'],
        "5": ['duplicates_'],
        "6": ['amounts_references_matched_'],
        "7": ['amounts_dates_matched_']
    }
    return variations[str(result_type)]