from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, fan of Tata Vence Batalla'

@app.route('/about')
def aboutus():
    return 'So you want information about us right?'

@app.route('/store')
def ourStore():
    return 'Welcome to the Store.'
