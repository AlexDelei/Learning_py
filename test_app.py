import pymysql
from flask import *
from flask_session import Session
import json
from pymysql import NULL
import smtplib
from email.message import EmailMessage
import secrets
import re
import datetime
from hello import get_hello_message, formatting, fib, time, get_last_login_time

app = Flask(__name__)

mysql = pymysql.connect(host= 'localhost', user= 'root', password= '', database= 'tester')
def insert_username(name, password):
    cur = mysql.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (name, password))
        mysql.commit()
        cur.close()
    except pymysql.IntegrityError:
        mysql.rollback()
        return False
    return True
def update_last_login_time(username):
    connection = pymysql.connect(host='localhost', user='root', password='', database='tester')
    cursor = connection.cursor()

    # Update the last_login field in the database for the user
    current_time = datetime.datetime.now()
    cursor.execute("UPDATE users SET last_login = %s WHERE username = %s", (current_time, username))
    connection.commit()
    cursor.close()
    connection.close()
def email_exists_in_database(email):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    result = cur.fetchone()
    cur.close()
    return result is not None
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
def name_exists_in_database(name):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (name))
    result = cur.fetchone()
    cur.close()
    return result is not None
def password_exists_in_database(password):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM users WHERE password = %s", (password))
    result = cur.fetchone()
    cur.close()
    return result is not None
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
        name = request.form['name']
        session['name'] = name
        password = request.form['password']
        name = name.title()

        connection = pymysql.connect(host='localhost', user='root', password='', database='tester')


        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM users WHERE username = %s AND password = %s''',  (name,password) )
        result = cursor.fetchall()

        if name == '':
                error_message8 = "Please insert your username"
                return render_template('login.html', message= message, message2=message2, error_message8 = error_message8)
        elif password == '':
                error_message7 = "Please insert your username and PASSWORD!"
                return render_template('login.html', message= message, message2=message2, error_message7 = error_message7)            
       # elif len(password) < 8:
        #    error_message9 = "Password must be atleast 8 characters"
         #   return render_template('login.html', message= message, message2=message2, error_message9 = error_message9)
        elif cursor.rowcount == 0:
            error_message4 = "Oops! Please confirm your details"
            return render_template ('login.html', error_message4 = error_message4)
        #elif name_exists_in_database(name, password) == 0:
         #   return redirect(url_for('error_page')) 
        else:
            update_last_login_time(name)
            return redirect(url_for('shoe_hub', name = name))
    return render_template('login.html')
 
@app.route('/shoehub', methods=['POST', 'GET'])
def shoe_hub():
        if 'name' not in session:
            return redirect('/login')

        name = session.get('name')
        last_time = get_last_login_time(name)
        c_time = time()
        time_ = c_time - last_time
        time_ = str(time_)
        time_ = time_.split(':')

        len_ = len(time_)
        for i in range(len_):
             if i == 0:
                  if int(time_[i]) != 0:
                       time_2 = time_[0]
                  else:
                       time_2 = time_[1]

        if request.method == 'GET':
            if name:
                name = name.split()
                length = len(name)
                if length == 1:
                    firstname = name[0]
                    len2 = len(name[0])
                    return render_template('products.html', firstname = firstname, len2 = len2, c_time = c_time, last_time = last_time,  time_2 = time_2)
                elif length >= 2:
                    firstname = name[1]
                    len2 = len(firstname)
                    render_template('products.html', firstname = firstname, len2 = len2, c_time = c_time, last_time = last_time,  time_2 = time_2)
                return render_template('products.html', firstname = firstname, len2 = len2 , last_time = last_time)
@app.route('/test')
def error_page():
    return render_template('test.html')
@app.route('/signin', methods=['POST', 'GET'])
def signin_boy():
     if request.method == 'GET':
          return render_template('signup.html')
     else:
          name = request.form['name']
          password = request.form['password']
          email = request.form['email']

          if len(name) == 0 and len(password) == 0:
               error3 = "You can not save null inputs, Please fill in your details"
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
            connection = pymysql.connect(host='localhost', password='', user='root', database='tester')
            cursor = connection.cursor()

            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (name, email, password))
            connection.commit()
            send_welcome_email(email, name) 
            saved = "Your details have been saved successfully, check your email"

            return render_template('signup.html', saved = saved)

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
     if request.method == 'GET':
          return render_template('update.html')
     else:
          name = session.get('name')
          current = request.form['current_pass']
          new = request.form['new_pass']

          if current == '' or new == '':
               error1 = "Please fill in all the details"
               return render_template('update.html', error1 = error1)
          elif current == new:
               error2 = "You have updated the same password"
               return render_template('update.html', error2 = error2)
          special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
          if not special_char_check.search(new):
               error3 = "Password must contain special characters"
               return render_template('update.html', error3= error3)

          
          connection = pymysql.connect(host='localhost', user='root', password='', database='tester')
          cursor = connection.cursor()

          cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (name, current))
          result = cursor.fetchone()

          if result:
            cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new, name))
            connection.commit()
            password_changed = "Password changed successfully"
            return render_template('update.html', password_changed=password_changed)
          else:
               incorrect = "Incorrect Password"
               return render_template('update.html', incorrect = incorrect)

          
   
if __name__ == '__main__':
    app.run(debug=True)