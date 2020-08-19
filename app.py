from flask import Flask
app = Flask(__name__)
# '/' denotes that we want to put our data at the root of our routes
@app.route('/')
def hello_world():
    return 'Hello world'
