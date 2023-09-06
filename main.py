from flask import Flask
from flask import render_template
from flask import request
import openai
import sys


from ask_question_to_pdf import *

app = Flask(__name__)


@app.route("/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=__name__)


@app.route("/prompt", methods=["POST"])
def promt():
    message = {}
    message["answer"] = gpt3_completion(request.form["prompt"])
    return message


@app.route("/question", methods=["GET"])
def question():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "Pose moi une question courte sur le cours."
    )
    return message





@app.route("/answer", methods=["POST"])
def answer():
    message = {}
    message["answer"] = ask_question_to_pdf("est-ce que ma reponse"+request.form["prompt"]+" est correcte?")
    return message


