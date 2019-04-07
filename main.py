from flask import Flask, request

app = Flask(__name__)
app .config['DEBUG'] = True


form = """

<!doctype html>
<html>
    <head>
        <h1>Signup</h1>
    </head>
    <body>
        <form>
            <label for= "username">Username</label>
            <input id="username" type = "text" />
            <br>
            <br>
            <label for= "password">Password</label>
            <input id="password" type="password" />
            <br>
            <br>
            <label for= "verify_password">Verify Password</label>
            <input id="verify_password" type="password" />
            <br>
            <br>
            <label for= "email">Email (optional)</label>
            <input id="email" type="text"/>
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
    return form

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return '<h1>Welcome, ' + username + '!</h1>'

app.run()
