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
        self.aluno.set_id_aluno = userId
        if(userId > 0):     
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



