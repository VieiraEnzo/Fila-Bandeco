from flask import Flask, render_template

app = Flask(__name__)

#Pagina inicial do projeto
@app.route("/")
def index():
    return render_template("index.html", popup = "none")


@app.route("/login")
def index_login():
    return render_template("regis_aluno.html", popup = "block")
    

app.run()

