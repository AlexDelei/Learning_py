import Flask
from hello import get_hello_message

app = Flask(__name__)

@app.rout('/')
def hello():
    message = get_hello_message()
    return "hello i am alex"

if __name__ == '__main__':
    app.run(debug=True)