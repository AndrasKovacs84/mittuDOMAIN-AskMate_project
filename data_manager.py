import csv
import os.path
import base64
import datetime
main_path = os.path.dirname(os.path.abspath(__file__))


# read file into a @table
#
# @file_name: string
# @table: list of lists of strings
# @idx: list of integer
def get_datatable_from_file(file_name, idx):
    try:
        if os.stat(file_name).st_size > 0:
            datatable = []
            with open(file_name, 'r') as datafile:
                datafile_reader = csv.reader(datafile, delimiter=';', skipinitialspace=True, lineterminator='\n')
                for row in datafile_reader:
                    row = decode_base64[idx]
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
# @idx: list of integer
def append_datatable_to_file(file_name, datalist, idx):
    with open((main_path + '/' + file_name), 'a', newline="") as csvfile:
        datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
        datafile_writer.writerow(datalist)


# write a @datatable into a file
#
# @file_name: string
# @datatable: list of lists of strings
# @idx: list of integer
def write_datatable_to_file(file_name, datatable, idx):
    datatable = encode_base64(datatable, idx)
    with open((main_path + '/' + file_name), 'w', newline="") as csvfile:
        datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
        for row in datatable:
            datafile_writer.writerow(row)


# encodig a list of list or a list of string
#
# @data: list of lists of string or list of string
# @idx: list of integer
def encode_base64(data, idx):
    if any(isinstance(sub, list) for sub in data):
        for i, row in enumerate(data):
            for num in idx:
                data[i][num] = base64.b64encode(b'{}'.format(row[num]))
        return data
    else:
        for num in idx:
            data[num] = base64.b64encode(b'{}'.format(data[num]))
        return data


# encodig a list of list or a list of string
#
# @data: list of lists of string or list of string
# @idx: list of integer
def decode_base64(data, idx):
    for num in idx:
        data[num] = base64.b64encode(b'{}'.format(data[num])
    return data


def decode_time(data_line):
    data[1] = str(datetime.datetime.fromtimestamp(int(data[1])))
    return date

def encode_time(data_line):

    pass
