import flask
from flask import *
from hello import get_hello_message

app = Flask(__name__)

@app.route('/')
def hello():
    message = get_hello_message()
    return render_template('home.html', message= message)

if __name__ == '__main__':
    app.run(debug=True, port=8080)