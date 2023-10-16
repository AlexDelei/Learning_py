import flask
from flask import *
from hello import get_hello_message, formatting

app = Flask(__name__)

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
    return render_template('home.html', name=name, message=message, message2=message2)

if __name__ == '__main__':
    app.run(debug=True)