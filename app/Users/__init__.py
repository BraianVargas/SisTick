from flask import Blueprint

usersBP = Blueprint('users_BP', __name__)

from . import routes


