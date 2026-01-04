# users.py

users = {}

def register_user(username, password):
    if username in users:
        return False
    users[username] = {
        "password": password,
        "saved_movies": []
    }
    return True

def login_user(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False