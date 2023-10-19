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
@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        message = get_hello_message()
        message2 = formatting()
        name = request.form['name']
        password = request.form['password']
        name = name.title()

        if name_exists_in_database(name, password):
            name2 = name.split()
            length = len(name2[1])
            firstname = name2[1]
            return render_template('signin.html', name = name, length = length, firstname = firstname)
        elif name_exists_in_database(name, password) == 0:
            return redirect(url_for('error_page'))  
@app.route('/error')
def error_page():
    return render_template('error.html')
@app.route('/signin', methods=['PUT', 'GET'])
def signin_boy():
    if request.method == 'PUT':
        data = json.loads(request.data)
        name = data.get('name')
        password = data.get('password')
        
        
        if name_exists_in_database(name, password) == 1:
            error = "User already exists"
            return render_template('signup.html', error = error)
        else:
            if insert_username(name, password):
                saved = "User data successfully saved"
                return render_template('signup.html', saved = saved)
            else:
                error2 = "Failed to save data"
                return render_template('signup.html', error2 = error2)   

    saved = "User data successfully saved"    
    return render_template('signup.html')
        
if __name__ == '__main__':
    app.run(debug=True)