import csv
import prompter_311

# check for all specified keys?
# check that all keys in jsonObj are keys in CSV file
# filter using list comprehension???
# get JSON input from a file
# output filtered items to a file

# debugging function
def printAll (data, title):
    print title
    count = 1
    for row in data: 
        line = str(count)
        count += 1
        for k, v in row.items():
            if k == 'id' or k == 'fiscal_year':
                line = line + ' ' + v
        print line
    print

# oldList -> list filtering on
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

# main
jsonInput = {"fiscal_year": [2018], "start_date": [""], "area": [""], "asset_type": ["Bridge"], "planning_status": ["In Progress"]}
jsonObj = fixFilter (jsonInput)

# should rename prompter_311
fname = prompter_311.getFileName ()
f_in = open (fname)

# csvData initially stores all the data from the reader
csvData = []
with f_in:

    # copy data from reader into csvData
    reader = csv.DictReader(f_in)

    csvRow = {}
    for dictRow in reader:
        csvData.append (dictRow)
   
    for fKey, fValues in jsonObj.items():
        csvData = filterItemsFromList (csvData, fKey, fValues)

    printAll (csvData, "filtered results")
