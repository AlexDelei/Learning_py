import pymysql
from flask import *
import json
from pymysql import NULL
from hello import get_hello_message, formatting, fib

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
def name_exists_in_database(name, password):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (name,password))
    result = cur.fetchone()
    cur.close()
    return result is not None
def delete_acc(name):
    cur = mysql.cursor()
    cur.execute("DELETE FROM users WHERE username = %s", (name,))
    mysql.commit()
    cur.close()
@app.route('/')
def hello():
    message = get_hello_message()
    message2 = formatting()
    message3 = fib()
    return render_template('home.html', message= message, message2=message2, message3=message3)
@app.route('/login', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        message = get_hello_message()
        message2 = formatting()
        name = request.form['name']
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
        elif cursor.rowcount == 0:
            error_message4 = "Oops! Please confirm your details"
            return render_template ('login.html', error_message4 = error_message4)
        #elif name_exists_in_database(name, password) == 0:
         #   return redirect(url_for('error_page')) 
        else:
            return redirect(url_for('shoe_hub', name = name))
    return render_template('login.html')
 
@app.route('/shoehub', methods=['POST', 'GET'])
def shoe_hub():
        if request.method == 'GET':
            name = request.args.get('name')
            name = name.split()
            length = len(name)
            if length == 1:
                firstname = name[0]
                len2 = len(name[0])
                return render_template('products.html', firstname = firstname, len2 = len2)
            elif length >= 2:
                firstname = name[1]
                len2 = len(firstname)
                render_template('products.html', firstname = firstname, len2 = len2)
            return render_template('products.html', firstname = firstname, len2 = len2 )
@app.route('/error')
def error_page():
    return render_template('error.html')
@app.route('/signin', methods=['POST', 'GET'])
def signin_boy():
    if request.method == 'POST':
        data = json.loads(request.data)
        name = data.get('name')
        password = data.get('password')

        connection = pymysql.connect(host='localhost', password='', user='root', database='tester')
        cursor = connection.cursor()
        if name_exists_in_database(name, password):
            error = "user already exists"
            return render_template('signup.html', error = error)
        else:
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (name, password))
                connection.commit()
                saved = "Your data has been successfully saved"
                if name == NULL:
                    error3 = "Insert your name!"
                    return render_template('signup.html', error3 = error3)
                
            except  pymysql.IntegrityError:
                error2 = "Failed to save data"
                return render_template('signup.html', error2 = error2)
    return render_template('signup.html')
        
if __name__ == '__main__':
    app.run(debug=True)