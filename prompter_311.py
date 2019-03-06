import os

# Assumes using .csv file
# Assumes there are files with .csv extension in the current directory
# Assumes want to use one of the .csv files in the current directory
# NB: I wanted to easily switch between test file and full data file
#   so I added this function to give me a list of .csv files in the current
#   directory so I wouldn't have to type in the full file name
def getFileName ():
    # get list of .csv files in the current directory
    # user will select a file name from this list
    listDir = []
    for f in os.listdir('.'):
        if (f[-4:].lower() == ".csv"):
            print (f)
            listDict = {'idx': len(listDir), 'fname': f}
            listDir.append (listDict)

    if len(listDir) == 0:
        return 'q'

    print (listDir)
    
    # get filename to use
    fname = ''
    while True:
        for listDict in listDir:
            print ("Type " + str(listDict['idx']) + " to use " + listDict['fname'] + ": ")
        response = input()
        if int(response) < len(listDir):
            selected = listDir[int(response)]
            print
            return selected['fname']
