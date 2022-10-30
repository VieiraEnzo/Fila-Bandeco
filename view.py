from flask import Flask, render_template, request
from control import Control

app = Flask(__name__)

#Pagina inicial do projeto
@app.route("/")
def index():
    return render_template("index.html", popup = "none")

#Pagina inicial com o popup de login
@app.route("/login_aluno")
def index_login_aluno():
    return render_template("index.html", popup = "block")

#Funcao para validar o Login de um Aluno
@app.route("/login_aluno", methods = ["POST"])
def index_login_aluno_post():
    identificador = request.form["identificador"]
    senha = request.form["senha"]
    return Control.valida_senha_aluno(identificador,senha)


#Site de Cadastro do aluno
@app.route("/regis_aluno")
def regis_aluno():
    return render_template("regis_aluno.html")

#Cadastra o aluno dentro do banco de dados
#adicionar outras exceções e usar try
@app.route("/regis_aluno", methods = ["POST"])
def regis_aluno_post():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    nome = nome + " " + sobrenome  #concatena o nome principal com o sobrenome
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    dre = request.form["dre"]
    senha = request.form["senha"]
    re_senha = request.form["re_senha"]
    a = Control()
    if senha == re_senha:         #compara se as senhas sao igual e retorna um erro se nao forem
        return a.registrar_aluno(nome, cpf, telefone, email, dre, senha)
    else:
        return render_template("regis_aluno.html", erro = "erroSENHA")



app.run()

