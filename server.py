import csv
import prompter
import ast
import json

def writeFilteredResults (data):
    f_out = open ('filtered_results.txt', 'w')
    f_out.write (json.dumps(data))

# debugging function
def printAll (data, title):
    print (title)
    count = 1
    for row in data: 
        line = str(count)
        count += 1
        for k, v in row.items():
            if k == 'id' or k == 'fiscal_year':
                line = line + ' ' + v
        print (line)
    print ()

# oldList -> the list that will be filtered on
# filterKey -> key value of interest for filtering
# filterValues -> list of string values or an empty list
def filterItemsFromList (oldList, filterKey, filterValues):
    # if filterValue is an empty list, do not filter on this key
    # so keep oldList by returning it
    if len(filterValues) == 0:
        return oldList

    newList = []
    for row in oldList:
        if row[filterKey] in filterValues:
            newList.append (row)
    return newList

# create a JSON object of filter values usable in this application
# specified format not usable as is:
# * 'status' field in CSV data called 'planning_status' in API
#	fix: convert 'planning_status' key to 'status'
# * default for an empty list is a list with one element
#	fix: use an empty list instead
# 
# Basically convert JSON default API from:
# {"fiscal_year": [-1], "start_date": [""], "area": [""], "asset_type": [""], 
#    "planning_status": [""]}
# to:
# {"fiscal_year": [], "start_date": [], "area": [], "asset_type": [], 
#    "status": []}
def fixFilter (jsonInput):
    jsonObj = {}

    for key, values in jsonInput.items():
        vList = []

        # for fiscal year, convert fields from integer to string
        if key == "fiscal_year":
            for v in values:
                if v != -1:
                    vList.append (str(v))

        # if no values specified, [""], use empty list, []
        # else use values as specified in jsonInput
        elif "" not in values:
            vList = values

        # if key is 'planning_status', convert it to 'status'
        # otherwise use speified key
        if key == "planning_status":
            jsonObj ["status"] = vList
        else:
            jsonObj [key] = vList

    return jsonObj

def validateJSON (jsonObj, csvKeys):
    for k in jsonObj.keys():
        if k not in csvKeys:
            return False
    return True

# main

# get JSON search object
jsonInputString = ""
fname = prompter.getFileName ("*.txt", "./inputFiles/jsonFiles", "Pick JSON Search Object file:")
f_json_in = open (fname, "r")
if f_json_in:
    jsonInputString = f_json_in.read()
    jsonInput = ast.literal_eval(jsonInputString) # crashes if invalid format
    f_json_in.close()
jsonObj = fixFilter (jsonInput) 

fname = prompter.getFileName ("*.csv", "./inputFiles/csvFiles", "Pick CSV file:")
f_csv_in = open (fname)

# csvData initially stores all the data from the reader
csvData = []
with f_csv_in:

    # copy data from reader into csvData
    reader = csv.DictReader(f_csv_in)
    csvRow = {}
    for dictRow in reader:
        csvData.append (dictRow)

    if validateJSON (jsonObj, csvData[0].keys()):
   
        # filter items in CSV file on the parameters specified in jsonObj
        for fKey, fValues in jsonObj.items():
            csvData = filterItemsFromList (csvData, fKey, fValues)

        writeFilteredResults (csvData)

    else:
        print ("Validation error in JSON search object")
