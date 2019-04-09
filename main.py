from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <style>
        .error {{ color: red; }}
    </style>
    <head>
        <h1>Signup</h1>
    </head>
    <body>
        <form method="POST">
            <label for= "username">Username</label>
            <input name="hours" id="username" type="text" value='{username}' />
            <p class = "error">{username_error}</p>
            <br>
            <br>
            <label for= "password">Password</label>
            <input name="password" id="password" type="password" value='{password}' />
            <p class = "error">{password_error}</p>
            <br>
            <br>
            <label for= "verify_password">Verify Password</label>
            <input name="verify_password" id="verify_password" type="password" value='{verify_password}' />
            <p class = "error">{verify_password_error}</p>
            <br>
            <br>
            <label for= "email">Email (optional)</label>
            <input name="email" id="email" type="text" value='{email}' />
            <p class = "error">{email_error}</p>
            <br>
            <br>
            <input type="submit" /> 
        </form>
    </body>
    <footer>
        <p>Form created by: Tracy Cook</p>
        <p>April 7, 2019</p>
        <p>LC101 User-Signup</p>
    </footer>
</html>

"""

@app.route("/")
def home():
    return form.format(username='', username_error='', password='', password_error='', verify_password='', verify_password_error='', email='', email_error='')


@app.route("/welcome")
def welcome():
    username = request.form['username']
    return '<h1>Welcome, ' + username + '!</h1>'






app.run()
