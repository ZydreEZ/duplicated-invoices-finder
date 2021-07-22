import search_duplicated_invoices
import files
import click


@click.command()
@click.option(
    "-i",
    "--input-folder",
    "input_folder",
    default='/data',
    help="Path to folder of invoices csv file(s) to be processed.",
    type=click.Path(dir_okay=True)
)
@click.option(
    "--out-dir",
    "-od",
    "out_dir",
    default="./duplicates",
    help="Path to csv files to store the result.",
    type=click.Path(dir_okay=True),
)
@click.option(
    "--out-file",
    "-of",
    "out_file",
    help="Name of csv files to store the result.",
    type=click.Path(dir_okay=False),
)
@click.option(
    "--result-type",
    "-rt",
    "result_type",
    default=1,
    help="Chose type of files which you want to save:\n"\
        '1 = will save 3 files (duplicates, amounts and references matched, amounts and dates matched)\n'\
        '2 = will save 2 files (duplicates, amounts and references matched)\n'\
        '3 = will save 2 files (duplicates, amounts and dates matched)\n'\
        '4 = will save 2 files (amounts and references matched, amounts and dates matched)\n'\
        '5 = will save 1 file (duplicates)\n'\
        '6 = will save 1 file (amounts and references matched)\n'\
        '7 = will save 1 file (amounts and dates matched)',
    type=int,
)

def process(input_folder, out_file, out_dir, result_type):
    user_choises = {
       "input_folder": input_folder,
       "out_file": out_file,
       "out_dir": out_dir,
       "result_type": result_type
    }
    all_invoices = files.read_files(input_folder)

    matched_invoices = search_duplicated_invoices.execute(all_invoices)
    
    files.write_to_file(all_invoices, matched_invoices, user_choises)


if __name__ == '__main__':
    process()

    