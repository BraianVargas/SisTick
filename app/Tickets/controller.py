import datetime
from Common.db import getDB

def createTicketHandler(dataDict):
    db, c  = getDB()
    
    keys, values = []
    for key,value in dataDict.items():
        keys.append(key)
        values.append(value)
    
    query = "INSERT INTO tickets"