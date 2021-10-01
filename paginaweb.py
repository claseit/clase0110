from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/nueva")
def bienvenido():
    return "<H1> Un titulo <H1>"

app.run()