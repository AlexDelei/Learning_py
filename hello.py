from flask import request, render_template

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