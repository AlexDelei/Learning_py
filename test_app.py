import pymysql
from flask import *
from pymysql import NULL
from hello import get_hello_message, formatting, signin_boy

app = Flask(__name__)

mysql = pymysql.connect(host= 'localhost', user= 'root', password= '', database= 'tester')
def insert_username(name, password):
    cur = mysql.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (name, password))
    mysql.commit()
    cur.close()
def name_exists_in_database(name, password):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (name,password))
    result = cur.fetchone()
    cur.close()
    return result is not None
@app.route('/')
def hello():
    message = get_hello_message()
    message2 = formatting()
    return render_template('home.html', message= message, message2=message2)
@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        message = get_hello_message()
        message2 = formatting()
        name = request.form['name']
        password = request.form['password']
        name = name.title()

        if name_exists_in_database(name, password):
            error_message = "Error: Name  already exists in database"
            length = len(name)
            return render_template('signin.html', name = name, length = length)
        elif name_exists_in_database(name, password) == 0:
            return redirect(url_for('error_page'))
    else:
        insert_username(name, password)
        success = "Name and password successfully stored in the database, its safe( * _ * )"
        return render_template('home.html', password = password, name = name, message = message, message2 = message2, success= success)   
@app.route('/error')
def error_page():
    return render_template('error.html')
@app.route('/signin')
def signin_boy():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)