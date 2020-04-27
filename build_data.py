import csv
import numpy as np
def parse_data(filename):
    name_token = "<name>"
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)[1:]

    parsed = []

    for row in data:
        parsed.append([row[4].replace(row[3], name_token), row[5].replace(row[3], name_token)])

    print(parsed[10])

    with open('desc1.tsv', 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in parsed:
            tsv_output.writerow(row)

def create_text(filename):
    s = ["", ""]

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)[1:]

    for row in data:
        s[0] += row[4]
        s[0] += row[5]
    with open('desc1.txt', 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='.')
        tsv_output.writerow(s)


#parse_data("descriptions1.csv")
create_text("descriptions1.csv")