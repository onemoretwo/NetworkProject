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

    host = "127.0.0.1"
    port = 20300

    weight = request.form["weight"]
    height = request.form["height"]

    pregnancies = request.form["pregnancies"]
    glucose = request.form["glucose"]
    bloodPressure = request.form["bloodPressure"]
    skinThickness = request.form["skinThickness"]
    insulin = request.form["insulin"]
    bmi = request.form["bmi"]
    diabetesPedigreeFunction = request.form["diabetesPedigreeFunction"]
    age = request.form["age"]

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