from ctypes import sizeof
from flask import render_template
from model import Aluno
from dao import AlunoDAO

class Control:
    def __init__(self):
        self.aluno = Aluno()
        self.aluno_logado = Aluno()
        self.alunoDAO = AlunoDAO()

    #Checa se o login do aluno é valido
    def login_aluno(self, identificador, senha):
        self.aluno.set_cpf(identificador)
        self.aluno.set_senha(senha)

        fetch = self.alunoDAO.efetuarLogin(self.aluno)

        if len(fetch) == 0:
            pass
        else:
            self.aluno_logado.set_id_aluno(fetch[0][0])
            self.aluno_logado.set_nome(fetch[0][1])
            self.aluno_logado.set_cpf(fetch[0][2])
            self.aluno_logado.set_telefone(fetch[0][3])
            self.aluno_logado.set_email(fetch[0][4])
            self.aluno_logado.set_senha(fetch[0][5])
            #fetch[0][6] é a data me que o aluno cadastro
            self.aluno_logado.set_dre(fetch[0][7])
        return fetch
        

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

    
    def agendar_aluno(self, aluno):
        pass


