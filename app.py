from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'If you are seeing this, Congratulations you sucessfully developed container'

@app.route('/health')
def health():
    return 'Server is up and running'
