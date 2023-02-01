import datetime
from Common.db import getDB
from flask_login import current_user

def createTicketHandler(dataDict):
    db, c  = getDB()
    
    keys=[]
    values = []
    for key,value in dataDict.items():
        keys.append(key)
        values.append(value)
    query = "INSERT INTO tickets ("
    for key in keys:
        if key == keys[-1]:
            query += f"creator_id, "
            query += f"{key})"
        else:
            query += f"{key},"

    query += " VALUES ("

    for value in values:
        if value == values[-1]:
            query += f"'{current_user.id}',"
            query += f"'{value}')"
        else:
            query += f"'{value}',"
    try:
        c.execute(query)
        db.commit()
        return "202 - Status Ok - Ticket Creado"
    except Exception as e:
        return f"FATAL ERROR. Tickets/Controller.py. Line 38 {e}"

