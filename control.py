from flask import render_template
from model import Aluno
from dao import AlunoDAO

class Control:
    aluno = None
    alunoDAO = None

    def __init__(self):
        self.aluno = Aluno()
        self.alunoDAO = AlunoDAO()

    #Checa se o login do aluno é valido
    #def valida_senha_aluno(self, identificador,senha):
        #if: ##########econtrou no banco de dados
            #return render_template("agendamento.html")
        #else:
            #return render_template("index.html", popup = "block", erro = "erroLOGIN")

    #Registra o aluno dentro do Banco de Dados
    def registrar_aluno(self, nome, cpf, telefone, email, dre, senha):
        #if: ###### cpf ja dentro do banco de dados
            #return render_template("regis_aluno.html", erro = "erroJALOGADO")
        #else:
            ##################### adicionar no banco de dados
        self.aluno.set_nome(nome)
        self.aluno.set_cpf(cpf)
        self.aluno.set_telefone(telefone)
        self.aluno.set_email(email)
        self.aluno.set_senha(senha)
        self.aluno.set_dre(dre)
        userId = self.alunoDAO.inserir(self.aluno)

        return render_template("index.html", errorVar = 0)

    
    #def inscricao_aluno_sessao(self, sessao):
        #if #####aluno inscrito em alguma sessao:
            #return render_template("agendamento.html", erro = "erroJAAGENDADO")
        #else:
            ####increver aluno na secao
            #eturn render_template("agendamento_completo.html")

    
    #def valida_senha_operador(self, identificador,senha):
        #if: ##########econtrou no banco de dados
            #return render_template("atendimento.html")
        #else:
            #return render_template("login_op.html", erro = "erroLOGIN")

