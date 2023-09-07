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
    message["answer"] = ask_question_to_pdf(request.form["prompt"])
    return message


@app.route("/question", methods=["GET"])
def question():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "Pose moi une question courte sur le cours."
    )
    return message


@app.route("/qcm", methods=["GET"])
def qcm():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "Pose un question difficile sur le texte. Tu proposeras UNIQUEMENT quatre réponses numérotées de A à D, dont une seule sera correcte, les autres seront fausses. Tu n'indiqueras pas la bonne réponse"
    )
    return message


# test


@app.route("/answer", methods=["POST"])
def answer():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "voici la question sur le texte :"
        + request.form["question"]
        + "est-ce que ma reponse"
        + request.form["prompt"]
        + " est correcte?"
    )
    return message


@app.route("/answerQCM", methods=["POST"])
def answerQCM():
    message = {}
    message["answer"] = ask_question_to_pdf(
        request.form["qcm"]
        + "Au vu de ces informations, répond seulement Vrai ou Faux (si Faux, indique la bonne réponse) à cette question : est-ce que la lettre"
        + request.form["prompt"]
        + " est celle de la bonne réponse à la question?"
    )
    return message
