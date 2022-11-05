from curses.ascii import NUL
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import control
from scrapper import Scrapper 

#Variável de ambiente encapsula o nome da aplicação dentro da variável app
app = Flask(__name__)
#Diz que a sessão não é permanente, logo quando o usuário fecha o browser ela sofre um 'destroy'
app.config["SESSION_PERMANENT"] = False
#Define que as sessões serão armazenadas através de um arquivo, o qual é armazenado no diretório flask_session
app.config["SESSION_TYPE"] = "filesystem"
#Instancia a sessão da aplicação
Session(app)

#Cria a rota para a página inicial do projeto
@app.route("/")
def index():
    return render_template("index.html")

#Rota para o cardápio
@app.route("/cardapio")
def cardapio():
    comidinhas = Scrapper.scrap()
    print(comidinhas)
    return render_template("cardapio.html", comidinhas = comidinhas)

#Rota para o sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

#Rota para a página locais
@app.route("/locais")
def locais():
    return render_template("locais.html")

#Rota para à página de cadastro do aluno
@app.route("/cadastro")
def cadastro_aluno():
    return render_template("cadastro.html")

#Rota para o envio do formulário de cadastro do aluno
#adicionar outras exceções e usar try
@app.route("/cadastro_aluno_post", methods = ["POST"])
def cadastro_aluno_post():
    #Recebe os valores dos inputs
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
    #Verifica o campo 'confirma senha'
    #Compara, se senhas iguais chama o controle e cadastra no banco
    #se senhas diferentes, retorna a página de cadastro com uma váriavel de erro
    #Atualizar para redirect e não render template
    if senha == re_senha:         
        return controle.registrar_aluno(nome, cpf, telefone, email, dre, senha)
    else:
        return render_template("cadastro.html", erro = "erroSENHA")
    
#Rota para a tela de agendamento
@app.route("/agendamento")
def agendamento():
    #Verifica se existe uma sessão, ou seja se o usuário está logado
    if session["alunoLogado"] == None:
        #Caso não haja uma sessão, redireciona para a página principal
        return redirect(url_for('index'))
    else:
        #Caso haja uma sessão, chama o controle para pegar as sessões disponíveis para agendamento
        sessao = control.sessaoControle.pegarTodos()
        #Retorna a página de agendamento com a variável contendo uma lista de todas as sessões
        return render_template("agendamento.html", sessaos = sessao)
    

#Rota para tentati de login do usuário
@app.route("/login_aluno", methods = ["POST"])
def login_aluno():
    #Atribui a variáveis os valores enviados pelo formulário
    identificador = request.form["identificador"]
    senha = request.form["senha"]
    #Instancia alunoControle
    controle = control.alunoControle()
    #Chama a função que verifica o login
    fetch = controle.login_aluno(identificador,senha)
    #verifica o retorno (Ambíguo, refazer com uma lógica mais enxuta)
    if fetch == None:
        #Retorna à página principal
        return redirect(url_for('index'))
    else:
        #Preenche a sessão com a instancia de aluno
        session["alunoLogado"] = fetch
        #Redireciona para a rota da página de agendamentos
        return redirect(url_for('agendamento'))

#Rota para a tela de registros de agendamentos
@app.route("/regis_agendamento")
def cadastro_agendamento():
    #Recebe o id da sessão através do URL (get)
    id_sessao = request.args.get('key', '')
    #Recebe o id do aluno através da sessão
    id_aluno = session["alunoLogado"].get_id_aluno()
    #Cria uma instancia de agendamentoControle
    controle = control.agendamentoControle()
    #Chama a função do controle que tenta realizar o agendamento e insere dentro de fetch
    fetch = controle.registrar_agendamento(id_aluno, id_sessao)
    #Caso o agendamento seja válido
    if fetch == True:
        return redirect(url_for('agendamento'))
    #Caso o agendamento seja inválido (criar exceção)
    else:
        return redirect(url_for('agendamento'))

#Cria a rota para o menu do agendamento, que lista os agendamento realizados pelo usuário
@app.route("/menu_agendamento")
def menu_agendamentos():
    #Verifica se existe uma sessão (pode ser uma função!?)
    if session["alunoLogado"] == None:
        return redirect(url_for('index'))
    else:
        #Chama um método estático que obtém todos os agendamento de determinado aluno
        agendamento = control.agendamentoControle.pegarPorId(session["alunoLogado"].get_id_aluno())
        #Retorna o menu de agendamento, com a lista de agendamentos
        return render_template("menu_agendamento.html", agendamentos = agendamento)

#Rota para a página principal do operador
@app.route("/operador")
def atendentePage():
    #Renderiza a página do operador
    return render_template("operador.html")

#Rota para a tentativa de login do operador
#app.post é igual a app.route(methods['POST'])
@app.post("/login_operador")
def login_operador():
    #Encapsula as variáveis enviadas através do formulário
    identificador = request.form["identificador"]
    senha = request.form["senha"]
    #Instancia o operadorControle
    controle = control.operadorControle()
    #Chama a função que tenta validar o login do operador
    fetch = controle.login_operador(identificador,senha)
    #Verifica se houve o retorno
    if fetch == None:
        #Caso retorno nulo, redireciona para a página do operador
        return redirect(url_for('atendentePage'))
    else:
        #cria a sessão do Operador
        session["operadorLogado"] = fetch
        #Redireciona para a rota de atendimento
        return redirect(url_for('atendimento'))

#Cria a rota do atendimento
@app.route("/atendimento")
def atendimento():
    #Verifica se a sessão do operador existe
    if session["operadorLogado"] == None:
        #Caso não exista redireciona para a página principal
        return redirect(url_for('index'))
    else:
        #Caso exista
        #Chama o método estático que retorna todos os atendimentos realizados por determinado operador
        atendimento = control.atendimentoControle.pegarPorOperador(session["operadorLogado"].get_id_operador()) 
        #Retorna a página de atendimento com a variável contendo a lista de atendimentos realizados
        return render_template("atendimento.html", atendimentos = atendimento)

#Cria a rota para o registro do atendimento
@app.post("/regis_atendimento")
def cadastro_atendimento():
    #Seta fetch como false
    fetch = False
    #Encapsula as variaǘeis enviadas pelo formulário
    tipoAtendimento = request.form["tipo"]
    cpf = request.form["cpf"]
    id_operador = session["operadorLogado"].get_id_operador()
    #Instancia o atendimentoControle
    controle = control.atendimentoControle()
    #Verifica o tipo de atentimento
    #Atendimento 2 = fila física
    if(tipoAtendimento == '2'):
        #pega o id_aluno através do cpf
        fk_id_aluno = control.alunoControle.pegarPorCpf(cpf)
        #pega o id_sessao da sessão válida que possue a unidade correspondente a unidade do Operador
        fk_id_sessao = control.sessaoControle.pegaPorUnidade(session["operadorLogado"].get_unidade())
    else:
        #Atemdimento 1 = Fila online
        #Pega o id_aluno através do CPF
        fk_id_aluno = control.alunoControle.pegarPorCpf(cpf)
        #Pega o id da sessao (complexa observar explicação em controle)
        fk_id_sessao = control.agendamentoControle.pegarValidaPorId(fk_id_aluno)

    #Chama a função que realiza o atendimento
    fetch = controle.registrar_atendimento(tipoAtendimento, fk_id_aluno, fk_id_sessao, id_operador) 

    #Verifica se o atendimento ocorreu ou nao (logica ruim reestruturar essa função)
    if(fetch == True):
        return redirect(url_for('atendimento'))
    else:
        return redirect(url_for('index'))

#Cria rota de logou
@app.route("/logout")
def logout():
    #Destrói a sessão atual
    session["alunoLogado"] = None
    #Redireciona para o index
    return redirect("/")
    
app.run()