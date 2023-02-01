from flask import Blueprint

ticketsBP = Blueprint('tickets_BP', __name__)

from . import routes


