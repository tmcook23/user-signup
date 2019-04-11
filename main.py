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
            <input name="username" id="username" type="text" value='{username}' /> <span class = "error">{username_error}</span>
            <br>
            <br>
            <label for= "password">Password</label>
            <input name="password" id="password" type="password" /> <span class = "error">{password_error}</span>
            <br>
            <br>
            <label for= "verify_password">Verify Password</label>
            <input name="verify_password" id="verify_password" type="password" /> <span class = "error">{verify_password_error}</span>
            <br>
            <br>
            <label for= "email">Email (optional)</label>
            <input name="email" id="email" type="text" value='{email}' /> <span class = "error">{email_error}</span>
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

@app.route("/", methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
        username_error = 'Enter a username'
        username = username
    elif ' ' in username: # IF USERNAME CONTAINS A SPACE:
        username_error = 'Usernames cannot contain spaces. Enter a valid username.'
        username = username
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Enter a valid username (3-20 characters).'
        username = username
    
    if password == '':
        password_error = 'Enter a password'
    elif ' ' in password: # IF PASSWORD CONTAINS A SPACE:
        password_error = 'Passwords cannot contain spaces. Enter a valid password.'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Enter a valid password (3-20 characters).'
    
    if verify_password != password:
        verify_password_error = 'Does not match password.'

    if email != '': # Email is optional, but if there is content in it, then it must be validated.
        if len(email) < 3 or len(email) > 20:
            email_error = 'Enter a valid email (3-20 characters).'
            email = email
        elif '@' not in email:
            email_error = 'Enter a valid email.'
            email = email
        elif '.' not in email:
            email_error = 'Enter a valid email.'
            email = email
        # The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return form.format(username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, password=password, verify_password=verify_password, email=email) #FROM EXAMPLE: hours=hours, minutes=minutes, etc.


# Creating an HTTP Redirect (must import redirect):

@app.route("/welcome")
def welcome():
    #username = request.form['username'] #request.form gets stuff from the body of the request (post request)
    #return '<h1>Welcome, ' + username + '!</h1>'
    username = request.args.get('username') #args.get gets stuff from query parameter
    return '<h1>Welcome, {0}!</h1>'.format(username)

app.run()
