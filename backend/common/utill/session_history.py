from flask import session

def set_history(user_UUID, messages):
    if user_UUID not in session:
        session[user_UUID] = []
    session[user_UUID].append(messages)
    
def get_history(user_UUID):
    if user_UUID not in session:
        session[user_UUID] = []
    return session[user_UUID]    
    