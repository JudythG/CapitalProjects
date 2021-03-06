import csv
import prompter

# main

fname = prompter.getFileName ("*.csv", "./inputFiles/csvFiles", "Select CSV File")
f_in = open (fname)

with f_in:
    reader = csv.DictReader(f_in)
    uniqueFields = {}
    for dictRow in reader:
        for key, value in dictRow.items():
            value = value.strip()
            if (len(value)):
                if key not in uniqueFields:
                    uniqueFields[key] = [value]
                elif value not in uniqueFields[key]:
                    uniqueFields[key].append(value)

    f_out = open ('uniqueFields.txt', "w")
    for header in uniqueFields.keys():
        f_out.write (header + "\n")
        for value in sorted(set(uniqueFields[header])):
            f_out.write ("\t" + value + "\n")
