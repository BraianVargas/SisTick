from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, username, email, password, type='usuario'):
        self.id = id
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.type = type
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def get_id(self):
        return super().get_id()

