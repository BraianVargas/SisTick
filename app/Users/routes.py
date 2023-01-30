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
    username = request.args.get('username')
    password = request.args.get('password')
    
    users = verifLogin(username,password)
    
    print(users)
    input()
    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        return redirect('/')
    return 'Invalid username or password'

#Desloguea al usuario
@usersBP.route('/logout')
@login_required
def logout():
    logout_user()
    return "Cerro sesion"


@usersBP.route('/register')
def registerUser():
    data = (request.get_json())
    statMessage = createNewUser(data)
    print(statMessage)
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