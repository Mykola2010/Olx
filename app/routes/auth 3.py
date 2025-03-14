from flask import Flask, session
from flask_httpauth import HTTPBasicAuth
import bcrypt


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": bcrypt.hashpw("AlexHome2010".encode(), bcrypt.gensalt()).decode()
}

@auth.verify_password
def verify_password(username, password):
    if username in users and bcrypt.checkpw(password.encode(), users[username].encode()):
        session["user"] = username
        return username
    return None

@app.get("/")
@auth.login_required
def index():
    return f"Hello {auth.current_user()}"

app.run()