import csv
import glob
import os
import pathlib
from datetime import datetime


def read_files():
    posted_invoices_list = []  

    for file_name in glob.glob('./data/*.csv'): 
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";") 
            for row in reader: 
                posted_invoices_list.append(row) 
    return posted_invoices_list

def write_to_file(posted_invoices_list, matched_invoices, file_name=False):
    """default file_name is like: duplicates_20210711_180344.csv"""
    name_variations = ['duplicates_', 'amounts_references_matched_', 'amounts_dates_matched_']
    header = list(posted_invoices_list[0].keys())
    empty_row = {}
    for key in header:
        empty_row[key] = None
    for variation in name_variations:
        name = variation + datetime.now().strftime("%Y%m%d_%H%M%S")
        with open('./duplicates/' + name + '.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, delimiter=";", fieldnames=header)
            writer.writeheader()
            for pair in matched_invoices[variation]:
                for ele in pair:
                    writer.writerow(posted_invoices_list[ele])
                writer.writerow(empty_row)