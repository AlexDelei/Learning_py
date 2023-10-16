import pymysql
from flask import *
from hello import get_hello_message, formatting

app = Flask(__name__)

mysql = pymysql.connect(host= 'localhost', user= 'root', password= '', database= 'tester')
def insert_username(name):
    cur = mysql.cursor()
    cur.execute("INSERT INTO users (username) VALUES (%s)", (name,))
    mysql.commit()
    cur.close()
def name_exists_in_database(name):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (name,))
    result = cur.fetchone()
    cur.close()
    return result is not None
@app.route('/')
def hello():
    message = get_hello_message()
    message2 = formatting()
    return render_template('home.html', message= message, message2=message2)
@app.route('/process', methods=['POST'])
def process():
    message = get_hello_message()
    message2 = formatting()
    name = request.form['name']
    name = name.title()

    if name_exists_in_database(name):
        error_message = "Error: Name  already stored in database"
        length = len(name)
        return render_template('signin.html', name = name, length = length)
    else:
        insert_username(name)
        success = "Name successfully stored in the database, its safe( * _ * )"
        return render_template('home.html', name = name, message = message, message2 = message2, success= success)

if __name__ == '__main__':
    app.run(debug=True)