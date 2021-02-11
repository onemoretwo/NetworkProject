from flask import Flask
from flask import render_template
import socket
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "main.html"
    )

@app.route("/predict", methods=["POST"])
def predict():

    host = socket.gethostname()
    port = 20300

    weight = request.form["weight"]
    height = request.form["height"]

    addr = (host, port)
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((addr))

    print("start client")

    cli.send(height.encode())

    data = cli.recv(4096).decode()

    cli.close()

    return render_template(
        "test.html",
        weight = weight,
        height = data
    )