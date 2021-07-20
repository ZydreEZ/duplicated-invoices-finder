import search_duplicated_invoices
import files

if __name__ == '__main__':
    posted_invoices_list = files.read_files()

    matched_invoices = search_duplicated_invoices.execute(posted_invoices_list)
    
    files.write_to_file(posted_invoices_list, matched_invoices)
