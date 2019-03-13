# CapitalProjects

Server to filter City of Pittsburgh <a href="https://data.wprdc.org/dataset/capital-projects">Capital Projects CSV data</a>. 

## Input
File that defines a JSON search object. Search criteria fields: project fiscal year, start date, area, asset type, and planning status.

JSON-encoded search criteria format showing default values: {"fiscal_year":[-1', "start_date":[""], "area": [""], "asset_type":[""], "planning_status":[""]}

To get a list of unique values for the JSON search fields, run getUniqueFromCSV.py
CSV headers are the same as the keys of the JSON search object except that "planning_status" in the JSON search object maps to "status" in the Capital Projects CSV file 

CSV file downloaded from the Capital Projects site

Note: input files are stored in sub-directories off of the directory where the server is run.

JSON files: ./inputFiles/jsonFiles/
JSON files are text files, *.txt

CSV files: ./inputFiles/csvFiles/

## Build With
Run with python3

## Written for
CCAC Python 2 course

