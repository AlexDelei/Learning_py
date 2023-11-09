import pymysql
from flask import *
from flask_session import Session
import json
from pymysql import NULL
import smtplib
from email.message import EmailMessage
import secrets
from secrets import *
import re
import datetime
from hello import get_hello_message, formatting, fib, time, get_last_login_time

app = Flask(__name__)

mysql = pymysql.connect(host='localhost', user='root', password='', database='tester')

def execute_query(query, values=None):
    try:
        with mysql.cursor() as cursor:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            result = cursor.fetchall()  # Fetch the result if required
            mysql.commit()
            return result  # Return the result if needed
    except pymysql.Error as e:
        print(f"Error executing query: {e}")
        mysql.rollback()

def insert_username(name, password):
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        execute_query(query, (name, password))
        return True
    except pymysql.IntegrityError:
        print("Error: Integrity Error occurred")
        return False
def update_last_login_time(email):
    # Update the last_login field in the database for the user
    current_time = datetime.datetime.now()
    execute_query("UPDATE users SET last_login = %s WHERE email = %s", (current_time, email))

def email_exists_in_database(email):
   result = execute_query("SELECT * FROM users WHERE email = %s", (email,))
   return bool(result)
def save_token_in_database(email, generated_token):
    try:
        query = "SELECT * FROM users WHERE email = %s"
        result = execute_query(query, (email,))

        if result:
            update_query = "UPDATE users SET token = %s WHERE email = %s"
            execute_query(update_query, (generated_token, email))
        else:
            insert_query = "INSERT INTO users (email, token) VALUES (%s, %s)"
            execute_query(insert_query, (email, generated_token))

    except pymysql.Error as e:
        print(f"Error: {e}")
def send_welcome_email(email_address, name):
    # Set up the email parameters
    name = name
    msg = EmailMessage()
    email_content = f"""
    <html>

    <body>
        <p>Hi {name}, Welcome to shoeCo!</p>
        <p>Thank you for joining us.</p>
        <img src="https://cdn.pixabay.com/photo/2023/10/29/22/11/leaves-8351230_640.jpg" alt="Shoehub Logo">
    </body>
    </html>
    """

    msg.add_alternative(email_content, subtype='html')

    msg['Subject'] = 'Welcome to shoeCo'
    msg['From'] = 'SHOECO254@gmail.com'  # Replace with your email
    msg['To'] = email_address

    # Set up SMTP connection and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # Replace with your SMTP server details
        smtp.starttls()
        smtp.login('SHOECO254@gmail.com', 'mpaz mtfb isli mxfh')  # Replace with your email credentials
        smtp.send_message(msg)
def pass_update_email(email_address, name):
    # Set up the email parameters
    msg = EmailMessage()
    email_content = f"""
    <html>

    <body>
        <p>Hi {name},</p>
        <p>You successfully changed your password</p>
        <p>If this wasnt you please ensure you update your password as soon as possible ASAP or contact us via support254@gmail.com</p>
        <img src="https://cdn.pixabay.com/photo/2023/10/29/22/11/leaves-8351230_640.jpg" alt="Shoehub Logo">
    </body>
    </html>
    """

    msg.add_alternative(email_content, subtype='html')

    msg['Subject'] = 'PASSWORD CHANGE'
    msg['From'] = 'SHOECO254@gmail.com'  # Replace with your email
    msg['To'] = email_address

    # Set up SMTP connection and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # Replace with your SMTP server details
        smtp.starttls()
        smtp.login('SHOECO254@gmail.com', 'mpaz mtfb isli mxfh')  # Replace with your email credentials
        smtp.send_message(msg)
def save_reset_token_in_database(email, token):

    # Save the reset token for the specific email in the database
    execute_query("UPDATE users SET reset_token = %s WHERE email = %s", (token, email))

def send_reset_email(email, reset_token):
    # Set up the email parameters
    msg = EmailMessage()
    reset_link = f"http://127.0.0.1:5000/test?token={reset_token}"  # Replace with your actual website URL

    email_content = f"""
    <html>
    <body>
        <p>To reset your password, please click the following link:</p>
        <a href="{reset_link}">Reset Password</a>
    </body>
    </html>
    """

    msg.add_alternative(email_content, subtype='html')

    msg['Subject'] = 'Password Reset Request'
    msg['From'] = 'SHOECO254@gmail.com'  # Replace with your email
    msg['To'] = email

    # Set up SMTP connection and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # Replace with your SMTP server details
        smtp.starttls()
        smtp.login('SHOECO254@gmail.com', 'mpaz mtfb isli mxfh')  # Replace with your email credentials
        smtp.send_message(msg)
def name_exists_in_database(name):
    result = execute_query("SELECT * FROM users WHERE username = %s", (name))
    return bool(result)
def password_exists_in_database(password):
    result = execute_query("SELECT * FROM users WHERE password = %s", (password))
    return bool(result)
def get_username_from_email(email):


    # Check if the email exists in the database
    result = execute_query("SELECT username FROM users WHERE email = %s", (email,))
    return result[0] if result else None
    #if result:
        # Email exists, return the associated username
     #   return result[0]  # Assuming username is the first column retrieved in the query result
    #else:
        # Email doesn't exist in the database
     #   return None
def delete_acc(name):
    cur = mysql.cursor()
    cur.execute("DELETE FROM users WHERE username = %s", (name,))
    mysql.commit()
    cur.close()
app.secret_key = "AW_r%@jN*HU4AW_r%@jN*HU4AW_r%@jN*HU4"

@app.route('/')
def hello():
    message = get_hello_message()
    message2 = formatting()
    message3 = fib()
    c_time = time()
    return render_template('home.html', message= message, message2=message2, message3=message3, c_time = c_time)
@app.route('/login', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        message = get_hello_message()
        message2 = formatting()
        c_time = time()

        email = request.form['email']
        password = request.form['password']


        username = get_username_from_email(email)
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        result = execute_query(query, (email, password))
        if email == '':
                error_message8 = "Please insert your email"
                return render_template('login.html', message= message, message2=message2, error_message8 = error_message8)
        elif password == '':
                error_message7 = "Please fill in all the details"
                return render_template('login.html', message= message, message2=message2, error_message7 = error_message7)
        elif not result:
            error_message4 = "Oops! Please confirm your details"
            return render_template ('login.html', error_message4 = error_message4)
        else:
           # update_last_login_time(email)
           if username:
            generated_token = token_urlsafe(70)
            save_token_in_database(email, generated_token)
            session['token'] = generated_token
            token = generated_token
            session['email'] = email
            session['name'] = username
            if token:
                return redirect(url_for('shoe_hub', token = token, username = username))
            else:
                token_err = "Token not found. Please log in again."
                return render_template('login.html', token_err = token_err)
            
    return render_template('login.html')
 
@app.route('/shoehub/<token>', methods=['POST', 'GET'])
def shoe_hub(token):
        if request.method == 'GET':
             name = request.args.get('username')
             name = name.split()
             #len_ = len(name)
             if name:
                  f_name = name[0]
                  return render_template('products.html', f_name = f_name)
             else:
                  #f_name = name[1]
                  return render_template('products.html')
@app.route('/test', methods=['GET', 'POST'])
def error_page():
    if request.method == 'GET':
        return render_template('test.html')
    else:
        name = request.form['name']

        return render_template('test.html', name = name)
@app.route('/signin', methods=['POST', 'GET'])
def signin_boy():
     if request.method == 'GET':
          return render_template('signup.html')
     else:
          name = request.form['name']
          password = request.form['password']
          email = request.form['email']
          session['name'] = name
          session['password'] = password

          if len(name) == 0 and len(password) == 0:
               error3 = "Please fill in your details"
               return render_template('signup.html', error3= error3)
          elif len(name) == 0:
               error4 = "Please insert a username"
               return render_template('signup.html', error4 = error4)
          elif len(password) < 8:
               error2 = "Password must be atleast 8 charatacters"
               return render_template('signup.html', error2 = error2)
          elif name_exists_in_database(name):
               error = "User already exists"
               return render_template('signup.html', error = error)
          elif password_exists_in_database(password):
               error = "User already exists"
               return render_template('signup.html', error = error)
          if '@' not in email:
               error6 = "Please enter a valid email"
               return render_template('signup.html', error6 = error6)
          elif email_exists_in_database(email):
               error7 = "User Email already exists"
               return render_template('signup.html', error7 = error7) 
          special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
          if not special_char_check.search(password):
               error5 = "Password must contain special characters"
               return render_template('signup.html', error5= error5)
          else:
            execute_query("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (name, email, password))
            send_welcome_email(email, name)
            session['email'] = email
            saved = "Your details have been saved successfully, check your email"
            return render_template('signup.html', saved = saved, email = email)

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
     if request.method == 'GET':
          return render_template('update.html')
     else:
          name = session.get('name')
          email = session.get('email')          
          current = request.form['current_pass']
          new = request.form['new_pass']
          name = list(name)
          name = name[0]

          if current == '' or new == '':
               error1 = "Please fill in all the details"
               return render_template('update.html', error1 = error1)
          elif current == new:
               error2 = "You have updated the same password"
               return render_template('update.html', error2 = error2)
          elif len(new) < 8:
               error4 = "Password must be atleast 8 characters"
               return render_template('update.html', error4 = error4)
          special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
          if not special_char_check.search(new):
               error3 = "Password must contain special characters"
               return render_template('update.html', error3= error3)

          query = "SELECT * FROM users WHERE email = %s AND password = %s"
          result = execute_query(query, (email, current))

          if result:
            execute_query("UPDATE users SET password = %s WHERE email = %s", (new, email))
            saved = "Successfully updated password, check your email"
            pass_update_email(email, name)
            return render_template('update.html', saved = saved)
          else:
               incorrect = "Incorrect Password"
               return render_template('update.html', incorrect = incorrect, email = email)

          
@app.route('/new_pass', methods=['POST', 'GET'])
def new_password():
    if request.method == 'GET':
        hello = "Hello"
        return render_template('new_pass.html', hello = hello)  # A HTML form to take the user's email

    if request.method == 'POST':
        email = request.form['email']

        if not email:
            error_message = "Please provide your email address."
            return render_template('new_pass.html', error_message=error_message)

        if not email_exists_in_database(email):
            error_message = "Email does not exist in our records."
            return render_template('new_pass.html', error_message=error_message)

        # Generate a unique token or link and send it to the user's email
        # Functions to create a token and a function to send a reset link via email
        reset_token = secrets.token_urlsafe(30)  # Generating a unique token ( can adjust the token length)
        save_reset_token_in_database(email, reset_token)  # Save the token in the database
        send_reset_email(email, reset_token)  # Send an email with a link containing the token

        success_message = "An email with instructions to reset your password has been sent."
        return render_template('new_pass.html', success_message=success_message)

    return render_template('new_pass.html')
if __name__ == '__main__':
    app.run(debug=True)