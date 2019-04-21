from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask (__name__)
app.config ['DEBUG'] = True

# ROUTE TO DISPLAY THE FORM
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form ['username'] 
    password = request.form ['password']
    verify_password = request.form ['verify_password']
    email = request.form ['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if  username == "":
        username_error = "The field must not be blank!"
        username = username
    else:
        username = username
        if (len(username) < 3) or (len(username) > 20):
            username_error = 'Username must be 3-20 characters.'
            username = ''
              
   
            
                        
    if  password== "":
        password_error = 'Password must not be blank!'
        password = password
    else:
        password = password
        if (len(password) < 3) or (len(password) > 20):
            password_error = 'Password must be 3-20 characters and not contain spaces.'
            password = ''
                
    # if not len(password):
    #     password_error = 'Not a valid password'
    #     password = ''
            
    if password != verify_password:
        verify_password_error = 'Passwords must match.'
        verify_password = ''
    
    
    if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
        email_error = 'This is not a valid email. example: johndoe@john.com, or leave blank'
        email = ''        

            
                
    #no errors go to welcome if errors tell user errors show form

    if not (username_error or  password_error or verify_password_error or email_error):
                #return render_template ('welcome.html', username=username)
        return redirect('/welcome?username={0}'.format(username))
    else: 
        return render_template ('index.html', username=username, email=email,username_error=username_error, password_error=password_error,
                                    verify_password_error=verify_password_error, email_error=email_error)

#route confirmed user to welcome page 

@app.route('/welcome')
def valid_signup():

    username = request.args.get('username')
    return render_template('welcome.html', username=username)



app.run()    