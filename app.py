
from flask import (
    Flask, request, g
    )


app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

from Common.db import getDB
from flask_login import *
from app.Users.controller import *

# ----------------------------- GENERA EL ADMINISTRADOR DE LOGIN --------------------------------------
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    users = getAllUsers()
    for user in users:
        if user['id'] == int(user_id):
            user = User(user['id'], user['username'], user['email'], user['password'], user['type'])
            print(f"User from login manager {user}")
            return user
    return None


# ----------------------------- IMPORTA Y REGISTRA LOS BLUEPRINTS --------------------------------------
from app.Users import usersBP
app.register_blueprint(usersBP, url_prefix = '/users')



if __name__=="__main__":
    app.run()