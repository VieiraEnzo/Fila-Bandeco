from flask import Flask, render_template

app = Flask(__name__)

#Pagina inicial do projeto
@app.route("/")
def index():
    return render_template("index.html", var = "of")


@app.route("/login")
def index_login():
    return render_template("index.html", var = "on")
    

app.run()

