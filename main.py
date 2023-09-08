from flask import Flask
from flask import render_template
from flask import request
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


@app.route("/qcm", methods=["GET"])
def qcm():
    message = {}
    a = "Pose un question difficile sur le texte. Tu proposeras UNIQUEMENT"
    b = " quatre réponses numérotées de A à D, dont une seule sera correcte, "
    c = "les autres seront fausses. Tu n'indiqueras pas la bonne réponses"
    message["answer"] = ask_question_to_pdf(a + b + c)
    return message


# test


@app.route("/answer", methods=["POST"])
def answer():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "voici la question sur le texte :"
        + request.form["question"]
        + ". Est-ce que la reponse"
        + request.form["prompt"]
        + "correspond au document?"
    )
    return message


@app.route("/answerQCM", methods=["POST"])
def answerQCM():
    message = {}
    message["answer"] = ask_question_to_pdf(
        "voici la question sur le texte :"
        + request.form["qcm"]
        + "Répond seulement Vrai ou Faux (si Faux, indique la bonne réponse). Est-ce que la lettre"
        + request.form["prompt"]
        + " est celle de la bonne réponse à la question?"
    )
    return message
