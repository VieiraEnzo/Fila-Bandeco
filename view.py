from curses.ascii import NUL
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import control

comidinhas = ["arroz","arroz","arroz","arroz","arroz","arroz","arroz"]

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
<<<<<<< HEAD
        sessao = control.sessaoControle.pegarTodos()
        return render_template("agendamento.html", sessaos = sessao)
    
=======
        return render_template("agendamento.almoco.html")


@app.route("agendamento_refeicao")
def agendamento_jantar():
    horario = request.form.get("horario")
    return a.agendar_aluno(horario)




>>>>>>> 3d54eb67b8701d81133a8d2e06413295fd74a531

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
        return render_template("atendimento.html")

@app.post("/regis_atendimento")
def cadastro_atendimento():
    tipoAtendimento = request.form["tipo"]
    cpf = request.form["cpf"]
    id_operador = session["operadorLogado"].get_id_operador()
    if(tipoAtendimento == 2):
        controle = control.atendimentoControle()
        fk_id_sessao = control.sessaoControle.pegaValida()
        fk_id_aluno = control.alunoControle.pegaPorCpf()
        return controle.registrar_atendimento(tipoAtendimento, fk_id_aluno, fk_id_sessao, id_operador)
    else:
        pass

#Realiza o logout
@app.route("/logout")
def logout():
    session["alunoLogado"] = None
    return redirect("/")
    
app.run()