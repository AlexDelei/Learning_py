from flask import request, render_template
import datetime
import pymysql

def get_hello_message():
    text = "alex delei"
    x = text.split()   
    firstname = len(x)
    return firstname
def formatting():
    a, b, c = "yoghurt", "soda", "cake"
    f, g, h = 100, 180, 50
    items = "The prices of : {2} is {4} shillings, {1} for {5} shillings and {0} for {3} shillings only"
    result = items.format(a, b, c, f, g, h)
    print(result)
    return result.title()
def fib():
    person = {
        'Firstname' : 'Harry',
        'Secondname' : 'maguire',
        'age': 32
    }
    x = person.values()
    return x
def time():
    current_time = datetime.datetime.now()
    return current_time

number = 100
ldt = number % 100
lldt = ldt % 10
print("Last digit of %d is %d" % (number, lldt))

def get_last_login_time(email):
    connection = pymysql.connect(host='localhost', user='root', password='', database='tester')
    cursor = connection.cursor()

    cursor.execute("SELECT last_login FROM users WHERE email = %s", (email,))
    last_login = cursor.fetchone()

    cursor.close()
    connection.close()

    return last_login[0] if last_login else None