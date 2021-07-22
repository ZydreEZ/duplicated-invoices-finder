# Duplicated invoices finder

## Introduction

This project is for finding duplicated invoices. It reads csv files that contain invoices and looks for duplicates by the "reference number", "invoice date" and "gross amount" columns. The result is three types of csv files - "duplicates" (where are invoices with matched "reference number", "invoice date" and "gross amount"), "amounts and references matched" and "amounts and dates matched". There is invoices example files in project folder "/data".

## Technologies

Python 3.6+

## How to use

There is command line interface with options:
```
 -i, --input-folder PATH     Path to folder of invoices csv file(s) to be
                              processed.
  -od, --out-dir PATH         Path to csv files to store the result.
  -of, --out-file FILE        Name of csv files to store the result.
  -rt, --result-type INTEGER  Chose type of files which you want to save: 
                                1 = will save 3 files (duplicates, amounts and
                              references matched, amounts and dates matched) 
                                2 = will save 2 files (duplicates, amounts and
                              references matched) 
                                3 = will save 2 files 
                                (duplicates, amounts and dates matched) 
                                4 = will save 2 files (amounts and references matched, amounts and dates matched) 
                                5 = will save 1 file (duplicates) 
                                6 = will save 1 file (amounts and references matched) 
                                7 = will save 1 file (amounts and dates matched)
```
These options could be called with terminal command: `python -m cli --help`.
