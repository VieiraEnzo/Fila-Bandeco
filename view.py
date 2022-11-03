from curses.ascii import NUL
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import control
from scrapper import Scrapper 


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
    comidinhas = Scrapper.scrap()
    return render_template("cardapio.html", comidinhas = comidinhas)

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
    if senha == re_senha:         
        #compara se as senhas sao igual e retorna um erro se nao forem
        return controle.registrar_aluno(nome, cpf, telefone, email, dre, senha)
    else:
        return render_template("cadastro.html", erro = "erroSENHA")
    
#Pagina inicial com o login
@app.route("/agendamento")
def agendamento():
    if session["alunoLogado"] == None:
        return redirect(url_for('index'))
    else:
        sessao = control.sessaoControle.pegarTodos()
        return render_template("agendamento.html", sessaos = sessao)
    

#Funcao para validar o Login de um Aluno
@app.route("/login_aluno", methods = ["POST"])
def login_aluno():
    identificador = request.form["identificador"]
    senha = request.form["senha"]
    controle = control.alunoControle()
    fetch = controle.login_aluno(identificador,senha)
    if fetch == None:
        return redirect(url_for('index'))
    else:
        session["alunoLogado"] = fetch
        return redirect(url_for('agendamento'))

#Realizando o agendamento
@app.route("/regis_agendamento")
def cadastro_agendamento():
    id_sessao = request.args.get('key', '')
    id_aluno = session["alunoLogado"].get_id_aluno()
    controle = control.agendamentoControle()
    fetch = controle.registrar_agendamento(id_aluno, id_sessao)

    if fetch == True:
        return redirect(url_for('agendamento'))
    else:
        return redirect(url_for('agendamento'))

@app.route("/menu_agendamento")
def menu_agendamentos():
    if session["alunoLogado"] == None:
        return redirect(url_for('index'))
    else:
        agendamento = control.agendamentoControle.pegarPorId(session["alunoLogado"].get_id_aluno())
        return render_template("menu_agendamento.html", agendamentos = agendamento)

@app.route("/operador")
def atendentePage():
    return render_template("operador.html")

@app.post("/login_operador")
def login_operador():
    identificador = request.form["identificador"]
    senha = request.form["senha"]
    controle = control.operadorControle()
    fetch = controle.login_operador(identificador,senha)
    if fetch == None:
        return redirect(url_for('atendentePage'))
    else:
        session["operadorLogado"] = fetch
        return redirect(url_for('atendimento'))

@app.route("/atendimento")
def atendimento():
    if session["operadorLogado"] == None:
        return redirect(url_for('index'))
    else:
        atendimento = control.atendimentoControle.pegarPorOperador(session["operadorLogado"].get_id_operador()) 
        return render_template("atendimento.html", atendimentos = atendimento)

@app.post("/regis_atendimento")
def cadastro_atendimento():
    fetch = False
    tipoAtendimento = request.form["tipo"]
    cpf = request.form["cpf"]
    id_operador = session["operadorLogado"].get_id_operador()
    controle = control.atendimentoControle()
    if(tipoAtendimento == '2'):
        fk_id_aluno = control.alunoControle.pegarPorCpf(cpf)
        fk_id_sessao = control.sessaoControle.pegaPorUnidade(session["operadorLogado"].get_unidade())
    else:
        fk_id_aluno = control.alunoControle.pegarPorCpf(cpf)
        fk_id_sessao = control.agendamentoControle.pegarValidaPorId(fk_id_aluno)

    
    fetch = controle.registrar_atendimento(tipoAtendimento, fk_id_aluno, fk_id_sessao, id_operador) 

    if(fetch == True):
        return redirect(url_for('atendimento'))
    else:
        return redirect(url_for('index'))

#Realiza o logout
@app.route("/logout")
def logout():
    session["alunoLogado"] = None
    return redirect("/")
    
app.run()