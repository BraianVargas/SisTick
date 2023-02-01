import datetime
from flask import (
    request, 
    Flask,
    request
)
from flask_login import(
    login_required,
    current_user
)
from .controller import *
from . import ticketsBP

@ticketsBP.route('/nuevo', methods=['GET', 'POST'])
def createTicket():
    data = request.get_json()
    
    try:
        statMessage = createTicketHandler(data)
        return statMessage
    except Exception as e:
        return f"Error in file routes.py -> tickets/nuevo. {e}"
