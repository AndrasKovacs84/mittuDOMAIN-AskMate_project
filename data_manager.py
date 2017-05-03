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
                    if row[0] != "ID":
                        row = decode_base64(row, idx)
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
    datalist = encode_base64(datalist, idx)
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
                data[i][num] = base64.b64encode(row[num].encode("utf-8"))
        return data
    else:
        for num in idx:
            data[num] = base64.b64encode(data[num].encode("utf-8"))
        return data


# encodig a list of list or a list of string
#
# @data: list of lists of string or list of string
# @idx: list of integer
def decode_base64(data, idx):
    for num in idx:
        data[num] = base64.b64decode(data[num]).decode("utf-8")
    return data


# decoding unix timestamp use before display
#
# @data_line: list of strnig
def decode_time(time_to_date):
    time_to_date = str(datetime.datetime.fromtimestamp(int(time_to_date)).strftime('%Y-%m-%d %H:%M:%S'))
    return time_to_date


def get_unixtime():
    return int(time.time())

"""
def encode_time(data_line):

    pass
"""
