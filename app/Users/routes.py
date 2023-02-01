import datetime
from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from Common.db import getDB
from flask import Flask, render_template, request, session, redirect
from werkzeug.security import check_password_hash, generate_password_hash


from .models import User

from .controller import *
from . import usersBP
import time

#Login
@usersBP.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return f"Is already logged in. {current_user.username}"
    else:
        recivedUserData = request.get_json()
        try:
            user = getUserFromLogin(recivedUserData['username'], recivedUserData['password'])

            if ((user!=None) and (isinstance(user,User))):
                login_user(user, remember = recivedUserData['remember'], duration = datetime.timedelta(minutes=15))
                return f"Se pudo loguear {user.username}"
            else:
                return "No es de tipo usuario"
        except Exception as e:
            return f"User or password wrong. Error.{e}"

#Desloguea al usuario
@usersBP.route('/logout')
@login_required
def logout():
    logout_user()
    return "Cerro sesion"


@usersBP.route('/register', methods=['GET','POST'])
def registerUser():
    data = (request.get_json())
    statMessage = createNewUser(data)
    return statMessage


# ----------------------------- BUSQUEDAS Y FILTROS --------------------------------------

@usersBP.route('/getusers', methods=["GET","POST"])
@login_required
def getUsers():
    users = getAllUsers()
    if users != None:
        return users
    else:
        return "404 - User Table Is Empty"

@usersBP.route("/search", methods=['GET','POST'])
@login_required
def searchUser():
    #Se recibe el argumento como KEY
    i = get_users(request.get_json())
    return i

@usersBP.route('/new', methods = ["POST"])
@login_required 
def createUser():
    
    data = request.get_json()

    message = createNewUser(data)

    return message
    

@usersBP.route('/')
@login_required
def indexUsers():
    return "INDEX USER"
