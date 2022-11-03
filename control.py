from ctypes import sizeof
from flask import render_template
import model
import dao

class alunoControle:
    def __init__(self):
        self.aluno = model.Aluno()
        self.alunoDAO = dao.AlunoDAO()

    #Checa se o login do aluno é valido
    def login_aluno(self, identificador, senha):
        self.aluno.set_cpf(identificador)
        self.aluno.set_senha(senha)

        fetch = self.alunoDAO.efetuarLogin(self.aluno)

        if not fetch:
            return None
        else:
            self.aluno.set_id_aluno(fetch[0][0])
            self.aluno.set_nome(fetch[0][1])
            self.aluno.set_cpf(fetch[0][2])
            self.aluno.set_telefone(fetch[0][3])
            self.aluno.set_email(fetch[0][4])
            self.aluno.set_senha(fetch[0][5])
            #fetch[0][6] é a data me que o aluno cadastro
            self.aluno.set_dre(fetch[0][7])
            return self.aluno
        

    #Registra o aluno dentro do Banco de Dados
    def registrar_aluno(self, nome, cpf, telefone, email, dre, senha):
        self.aluno.set_nome(nome)
        self.aluno.set_cpf(cpf)
        self.aluno.set_telefone(telefone)
        self.aluno.set_email(email)
        self.aluno.set_senha(senha)
        self.aluno.set_dre(dre)
        userId = self.alunoDAO.inserir(self.aluno)
        if(userId > 0):
            self.aluno.set_id_aluno = userId
            return render_template("index.html", erro = 0)
        else:
            #adicionar exceção, pois como else não funciona
            return render_template("index.html", erro = "erroCadastro")

    
    def agendar_aluno(self):
        pass

class sessaoControle:
    def __init__(self):
        self.sessao = model.Sessao()
        self.sessaoDAO = dao.SessaoDAO()

    @staticmethod
    def pegarTodos():
        fetch = dao.SessaoDAO.pegarTodos()
        return fetch

class agendamentoControle:
    def __init__(self):
        self.agendamento = model.Agendamento()
        self.agendamentoDAO = dao.AgendamentoDAO()

    def registrar_agendamento(self, fk_id_aluno, fk_id_sessao):
        self.agendamento.set_statusAgendamento("Válido")
        self.agendamento.set_fk_id_aluno(fk_id_aluno)
        self.agendamento.set_fk_id_sessao(fk_id_sessao)
        userId = self.agendamentoDAO.inserir(self.agendamento)
        if(userId > 0):
            self.agendamento.set_id_agendamento = userId
            return True
        else:
            #adicionar exceção, pois como else não funciona
            return False

class operadorControle:
    def __init__(self):
        self.operador = model.Operador()
        self.operadorDAO = dao.OperadorDAO()

    #Checa se o login do operador é valido
    def login_operador(self, identificador, senha):
        self.operador.set_cpf(identificador)
        self.operador.set_senha(senha)

        fetch = self.operadorDAO.efetuarLogin(self.operador)

        if not fetch:
            return None
        else:
            self.operador.set_id_operador(fetch[0][0])
            self.operador.set_nome(fetch[0][1])
            self.operador.set_cpf(fetch[0][2])
            self.operador.set_telefone(fetch[0][3])
            self.operador.set_email(fetch[0][4])
            self.operador.set_senha(fetch[0][5])
            self.operador.set_unidade(fetch[0][6])
            return self.operador

class atendimentoControle():
    def __init__(self):
        self.atendimento = model.Atendimento()
        self.atendimentoDAO = dao.OperadorDAO()

    def validaAgendamento():
        pass

    
    def registrar_atendimento(self, tipoAtendimento, fk_id_aluno, fk_id_sessao, id_operador):
        self.atendimento.set_tipoAtendimento(tipoAtendimento)
        self.atendimento.set_fk_id_aluno(fk_id_aluno)
        self.atendimento.set_fk_id_sessao(fk_id_sessao)
        self.atendimento.set_fk_id_operador(id_operador)
        userId = self.atendimentoDAO.inserir(self.atendimento)
        if(userId > 0):
            self.agendamento.set_id_agendamento = userId
            return True
        else:
            #adicionar exceção, pois como else não funciona
            return False
    
    def realizaAtendimento(self, cpf, tipoAtendimento, id_operador):
        pass

