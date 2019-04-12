from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def home():
    return render_template('home.html')

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
        username_error = 'Enter a username.'
        username = username
    elif ' ' in username: # If username contains a space:
        username_error = 'Usernames cannot contain spaces. Enter a valid username.'
        username = username
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Enter a valid username (3-20 characters).'
        username = username
    
    if password == '':
        password_error = 'Enter a password.'
    elif ' ' in password: # If password contains a space:
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
        return render_template('home.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, password=password, verify_password=verify_password, email=email)

# Creating an HTTP Redirect (must import redirect):

@app.route("/welcome")
def welcome():
    username = request.args.get('username') # args.get gets stuff from query parameter
    # return .format(username)
    return render_template('welcome.html', username=username)

app.run()
