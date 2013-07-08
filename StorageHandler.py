import json

customers = {}
STATES = []

class Storage:
    def __init__(self, fileName):
        if(fileName is None or fileName == ''):
            loadDataDefault()
        else:
            loadData(fileName)
        
def loadDataDefault():
    global storage
    try:
        storageFile = open('database.json', 'r')
        fileString = ''
        for line in storageFile:
            fileString += line
        customers = json.loads(fileString)
    except IOError:
        print("Error reading file -- no such file exists. Creating")
        storageFile = open('database.json', 'w')
        storageFile.close()
        loadDataDefault()

def newCustomer(detailsJSON):
    valid = true
    if(not(inStateList(detailsJSON))):
        valid = false
    if(not('name' in detailsJSON)):
        valid = false
    

def inStateList(stateString):
    return false

def getStates():
    global STATES
    return STATES

