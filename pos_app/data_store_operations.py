import csv


def read_from_store(file_name):
    with open(file_name, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)


def write_to_store(file_name, data):
    with open(file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
