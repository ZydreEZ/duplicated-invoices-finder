import csv
import glob
import os
import pathlib
from datetime import datetime


# 1. read csv file
def read_files():
    posted_invoices_list = [] # create empty list for all invoices from files. 

    for file_name in glob.glob('./data/*.csv'): # glob method let to read all files from data folder. 
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";") 
            for row in reader: # read file rows as dictionaries
                posted_invoices_list.append(row) # add disctionaries to the list
    # print(posted_invoices_list)
    return posted_invoices_list

def write_to_file(posted_invoices_list, matched_invoices, file_name=False):
    """default file_name is like: duplicates_20210711_180344.csv"""
    name_variations = ['duplicates_', 'amounts_references_matched_', 'amounts_dates_matched_']
    header = list(posted_invoices_list[0].keys())
    empty_row = {}
    for key in header:
        empty_row[key] = None
    # if not file_name:
    # current_path = pathlib.Path(__file__).parent.resolve()
    # os.makedirs(os.path.dirname(current_path + '/duplicates/'), exist_ok=True)
    for variation in name_variations:
        name = variation + datetime.now().strftime("%Y%m%d_%H%M%S")
        with open('./duplicates/' + name + '.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, delimiter=";", fieldnames=header)
            writer.writeheader()
            for pair in matched_invoices[variation]:
                writer.writerow(posted_invoices_list[pair[0]])
                writer.writerow(posted_invoices_list[pair[1]])
                writer.writerow(empty_row)