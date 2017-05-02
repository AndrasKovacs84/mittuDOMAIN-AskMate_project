import csv
import os.path
import base64
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
                    row = decode_base64(row)
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
    datalist = encode_base64(datalist)
    with open((main_path + '/' + file_name), 'a', newline="") as csvfile:
        datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
        datafile_writer.writerow(datalist)


# write a @datatable into a file
#
# @file_name: string
# @datatable: list of lists of strings
def write_datatable_to_file(file_name, datatable):
    datatable = encode_base64(datatable)
    with open((main_path + '/' + file_name), 'w', newline="") as csvfile:
        datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
        for row in datatable:
            row = encode_base64(row)
            datafile_writer.writerow(row)


# encoding base64 charachter chain to string
#
# @data: list of string
def encode_base64(data):
    data[4] = base64.b64encode(b'{}'.format(data[4])
    data[5] = base64.b64encode(b'{}'.format(data[5])
    return data


# encoding base64 charachter chain to string
#
# @data: list of string
def decode_base64(data):
    data[4] = base64.b64decode(b'{}'.format(data[4])
    data[5] = base64.b64decode(b'{}'.format(data[5])
    return data
