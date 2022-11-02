from curses.ascii import NUL
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import control

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Pagina inicial do projeto
@app.route("/")
def index():
    return render_template("index.html")

#Roda a pagina do cardapio
@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

#roda a pagina do sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

#Pagina Locais
@app.route("/locais")
def locais():
    return render_template("locais.html")

#Site de Cadastro do aluno
@app.route("/cadastro")
def cadastro_aluno():
    return render_template("cadastro.html")

#Cadastra o aluno dentro do banco de dados
#adicionar outras exceções e usar try
@app.route("/cadastro_aluno_post", methods = ["POST"])
def cadastro_aluno_post():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    nome = nome + " " + sobrenome  #concatena o nome principal com o sobrenome
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    dre = request.form["dre"]
    senha = request.form["senha"]
    re_senha = request.form["re_senha"]
    controle = control.alunoControle()
    if senha == re_senha:         #compara se as senhas sao igual e retorna um erro se nao forem
        return controle.registrar_aluno(nome, cpf, telefone, email, dre, senha)
    else:
        return render_template("cadastro.html", erro = "erroSENHA")
    
#Pagina inicial com o login
@app.route("/login_aluno")
def index_login_aluno():
    return render_template("index.html")

#Funcao para validar o Login de um Aluno
@app.route("/login_aluno", methods = ["POST"])
def login_aluno():

    identificador = request.form["identificador"]
    senha = request.form["senha"]
    controle = control.alunoControle()
    fetch = controle.login_aluno(identificador,senha)
    if fetch == None:
        return render_template("index.html", erro = "erroLogin")
    else:
        session["alunoLogado"] = fetch
        sessao = control.sessaoControle.pegarTodos()
        return render_template("agendamento.html", sessaos = sessao)

@app.route("/regis_agendamento")
def cadastro_agendamento():
    

@app.route("/logout")
def logout():
    session["alunoLogado"] = None
    return redirect("/")
app.run()