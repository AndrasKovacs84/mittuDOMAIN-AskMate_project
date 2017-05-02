import csv
import os.path
main_path = os.path.dirname(os.path.abspath(__file__))


# read file into a @table
#
# @file_name: string
# @table: list of lists of strings
def get_datatable_from_file(file_name):
    try:
        if os.stat(file_name).st_size > 0:
            datatable = []
            with open(file_name, 'r') as datafile:
                datafile_reader = csv.reader(datafile, delimiter=';', skipinitialspace=True, lineterminator='\n')
                for row in datafile_reader:
                    datatable.append(row)
            return datatable
        else:
            return 0
    except OSError:
        return 0


# append a @datalist into a file
#
# @file_name: string
# @datalist: list of strings
def append_datatable_to_file(file_name, datalist):
    with open((main_path + '/' + file_name), 'a', newline="") as csvfile:
        datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
        datafile_writer.writerow(datalist)


# write a @datatable into a file
#
# @file_name: string
# @datatable: list of lists of strings
def write_datatable_to_file(file_name, datatable):
    with open((main_path + '/' + file_name), 'w', newline="") as csvfile:
        datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
        for row in datatable:
            datafile_writer.writerow(row)
