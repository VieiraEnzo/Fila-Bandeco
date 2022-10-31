from curses.ascii import NUL
from flask import Flask, render_template, request
from control import Control
from model import Aluno

app = Flask(__name__)
a = Control()

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

#Pagina inicial com o login
@app.route("/login_aluno")
def index_login_aluno():
    return render_template("index.html")

#Funcao para validar o Login de um Aluno
@app.route("/login_aluno", methods = ["POST"])
def login_aluno():

    
    identificador = request.form["identificador"]
    senha = request.form["senha"]
    fetch = a.login_aluno(identificador,senha)
    print(fetch)
    print(fetch[0][2])
    if(len(fetch) == 0):
        return render_template("index.html", erro = "erroLogin")
    else:
        return render_template("agendamento.html")
    

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
    if senha == re_senha:         #compara se as senhas sao igual e retorna um erro se nao forem
        return a.registrar_aluno(nome, cpf, telefone, email, dre, senha)
    else:
        return render_template("cadastro.html", erro = "erroSENHA")


@app.route("/agendamento", methods = ["POST"])
def agendamento():
    
    refeicao = request.form.get("refeicao")
    local = request.form.get("local")
    print(refeicao, local)
    if refeicao == None or local == None:
        return render_template("agendamento.html", erro = "erroSELECAO")
    elif refeicao == 'jantar':
        return render_template("agendamento.jantar.html")
    else:
        return render_template("agendamento.almoco.html")


    

app.run()