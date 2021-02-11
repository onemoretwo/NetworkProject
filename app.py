from flask import Flask
from flask import render_template
from socket import *
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "main.html"
    )

@app.route("/predict", methods=["POST"])
def predict():

    weight = request.form["weight"]
    height = request.form["height"]

    addr = ("localhost", 7000)
    cli = socket(AF_INET, SOCK_STREAM)
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

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")