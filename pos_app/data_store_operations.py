import csv


def read_from_store(file_name):
    read_list = []
    with open(file_name, mode="r") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            read_list.append(lines)
    return read_list


def write_to_store(file_name, data):
    with open(file_name, "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
