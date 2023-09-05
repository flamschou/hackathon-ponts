from flask import Flask
from flask import render_template
from flask import request
import openai
import sys

sys.path.append(
    "C:/ENPC/Projects/Hackaton Theodo/hackathon-ponts/src/utils/ask_question_to_pdf.py"
)
from ask_question_to_pdf import ask_question_to_pdf

app = Flask(__name__)


@app.route("/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=__name__)


@app.route("/prompt", methods=["POST"])
def promt():
    message = {}
    message["answer"] = ask_question_to_pdf(request.form["prompt"])
    return message


@app.route("/question", methods=["GET"])
def question():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "Pose moi une question courte sur le cours."
    )
    return message


# request.form["submit"] +


@app.route("/answer", methods=["POST"])
def answer():
    message = {}
    message["answer"] = ask_question_to_pdf("est-ce que ma reponse est correcte?")
    return message
