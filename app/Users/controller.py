from Common.db import getDB
import hashlib
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash


def createNewUser(userDict):
    db,c = getDB()

    q = "INSERT INTO usuarios "
    keys = []
    values = []
    for key,value in userDict.items():
        keys.append(key)
        if(key == 'password'):
            values.append(generate_password_hash(value,"sha256"))
        else:
            values.append(value)
    q += "("
    for key in keys:
        if key == keys[-1]:
            q += f"{key}"
        else:
            q += f"{key},"
    q += ")"
    q += " VALUES"
    q += "("
    for value in values:
        if value == values[-1]:
            q += f"'{value}'"
        elif type(value) == int or type(value) == float:
            q += f"{value},"
        else:
            q += f"'{value}',"
    q += ")"
    try:
        c.execute(q)
        db.commit()
        return "202 - Status Ok - Usuario Creado"
    except Exception as e:
        return F"FATAL ERROR. {e}"

def verifLogin(user, password):
    db, c = getDB()
    try:
        c.execute(f"SELECT * FROM usuarios WHERE username = %s",(user,))
        selectedUser = c.fetchone


    except Exception as e:
        return f"Fatal error: {e}"

def getUserFromLogin(uname, inputPassword):
    db, c = getDB()
    try:
        c.execute(f"SELECT * FROM usuarios WHERE username = %s",(uname,))
        userSelected = c.fetchone()
        
        if userSelected != None:
            try:
                if check_password_hash(userSelected['password'], inputPassword):
                    try:
                        return User(userSelected['id'], userSelected['username'], userSelected['email'], userSelected['password'], userSelected['type'])
                    except Exception as e:
                        return f"Fatal User Error. {e}"
                else:
                    return "Error. Usuario o contraseña incorrecto."    
            except Exception as e:
                return f"Error{e}"
        else:
            return "Error. Usuario o contraseña incorrecto."
    except Exception as e:
        return f"Error. {e}"

def getAllUsers():
    db, c = getDB()
    c.execute("SELECT * FROM usuarios ORDER BY id ASC")
    users = c.fetchall()
    return users

def get_users(userDict):
    db, c = getDB()
    filtered=[]
    query = "SELECT * FROM usuarios WHERE "
    flag = 0 # Bandera de posicion inicial
    try:
        for key,value in userDict.items():
            if flag == 0:
                query += f" {key} LIKE '%{value}%' "
                flag += 1
            else:
                query += f" || {key} LIKE '%{value}%' "
        c.execute(query)
        filtered = c.fetchall()
        if filtered != None:
            return filtered
        else:
            return "404 - No se encontró el usuario"
    except Exception as e:
        return f"Fatal Error. {e}"
