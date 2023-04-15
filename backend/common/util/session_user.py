from flask import session

def set_user(user_id):
    session['id'] = user_id
    
    
def get_user():
    if 'id' in session:
        return session['id']
    else:
        Exception("No user id in session")
    
    