from flask import Flask, request, redirect, render_template 
import os 
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index(): 
    return render_template('usersignup.html')
@app.route('/')
def no_entry(x):
    if x:
        return True
    else: 
        return False
def length_of_entry(x):
    if len(x) > 2 and len(x) < 20: 
        return True
    else: 
        return False

def at_symbol(x): 
    if x.count('@') == 1:
        return True
    else: 
        return False
def period_email(x): 
    if x.count('.') == 1: 
        return True
    else: 
        return False 

@app.route("/", methods=['POST'])
def form_finished(): 
    #fetch inputs from form using request 
    username = request.form['Username']
    password = request.form['Password']
    password_verify = request.form ['Verify_Password']
    email = request.form['Email']
    #create error message empty strings
    username_err = ""
    password_err = ""
    password_verify_err = ""
    email_err = ""
    #create error messages 
    required = "This is a required field"
    reenter = "Please re-enter your password"
    length = "must be between 3 and 20 characters long"
    spaces = "This field does not accept spaces"

    #Create validation if clauses for errors
    if not no_entry(password):
        password_err = required 
        password = ''
        password_verify = ''
    elif not length_of_entry(password):
        password_err = length 
        password = ''
        password_verify = '' 
        password_verify_err = reenter 
    else: 
        if " " in password: 
            password_err = spaces 
            password = ''
            pasword_verify = ''
            password_verify_err = reenter 
    
    if no_entry(email):
        password = ''
        password_verify = '' 
        if not length_of_entry(email): 
            email_err = "Email" + length 
            password_err = reenter
            password_verify = reenter 
        elif not at_symbol(email): 
            email_err = "Not a valid email. Try again."
            password_err = reenter
            password_verify_err = reenter 
        elif not period_email(email): 
            email_err = "Not a valid email. Try again."
            password_err = reenter
            password_verify_err = reenter
        else: 
            if " " in email: 
                email_err = "Email" + spaces 
                password_err = reenter
                password_verify_err = reenter
        if not username_err and not password_err and not password_verify_err and not email_err:
            return redirect ('/greeting') 
        else:
            return render_template('usersignup.html', username_err = username_err, username = username, password = password, password_err = password_err, password_verify_err = password_verify_err, password_verify = password_verify, Email = email, email_err = email_err)
@app.route('/greeting', methods = ['GET'])
def signup_complete(): 
    Username = request.args.get('Username')
    return render_template ('welcome.html', Username = Username )

app.run()


