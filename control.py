from ctypes import sizeof
from flask import render_template, redirect, url_for
import model
import dao

class alunoControle:
    #Instancia o Modelo
    #Instancia o DAO
    def __init__(self):
        self.aluno = model.Aluno()
        self.alunoDAO = dao.AlunoDAO()

    #Checa se o login do aluno é valido
    def login_aluno(self, identificador, senha):
        #Seta os atributos necessários para o login
        self.aluno.set_cpf(identificador)
        self.aluno.set_senha(senha)
        #Tenta efetuar o login e encapsula o retorno dentro de fetch
        fetch = self.alunoDAO.efetuarLogin(self.aluno)
        #Se não houve nenhum retorno
        if not fetch:
            return None
        #Se houve algum retorno
        else:
            #Seta o usuário
            self.aluno.set_id_aluno(fetch[0][0])
            self.aluno.set_nome(fetch[0][1])
            self.aluno.set_cpf(fetch[0][2])
            self.aluno.set_telefone(fetch[0][3])
            self.aluno.set_email(fetch[0][4])
            self.aluno.set_senha(fetch[0][5])
            #fetch[0][6] é a data me que o aluno cadastro
            self.aluno.set_dre(fetch[0][7])
            #Retorna o modelo aluno com os atributos setados
            return self.aluno
        

    #Registra o aluno dentro do Banco de Dados
    def registrar_aluno(self, nome, cpf, telefone, email, dre, senha):
        #Seta os atributos de aluno
        self.aluno.set_nome(nome)
        self.aluno.set_cpf(cpf)
        self.aluno.set_telefone(telefone)
        self.aluno.set_email(email)
        self.aluno.set_senha(senha)
        self.aluno.set_dre(dre)
        #Joga para a dao que realiza o cadastro e retorna o ID
        userId = self.alunoDAO.inserir(self.aluno)
        #O id é setado por padrão como -1
        #Se Id > 0, significa que houve o cadastro
        if(userId > 0):
            #seta o id do aluno
            self.aluno.set_id_aluno = userId
            #Redireciona pra index sem erro (mudar para redirect)
            return render_template("index.html", erro = 0)
        else:
            #Redireciona para index com erro, mudar para redirect
            return render_template("index.html", erro = "erroCadastro")

    #Método estático que retorna o id do aluno através do CPF
    @staticmethod
    def pegarPorCpf(cpf):
        #Estabele a conexão com o DAO
        fetch = dao.AlunoDAO.pegarPorCpf(cpf,)
        #Retorna o id_aluno
        return fetch[0][0]

class sessaoControle:
    def __init__(self):
        self.sessao = model.Sessao()
        self.sessaoDAO = dao.SessaoDAO()
    
    #Método estático que chama o DAO e requisita todas as sessões disponíveis
    @staticmethod
    def pegarTodos():
        fetch = dao.SessaoDAO.pegarTodos()
        print(fetch)
        return fetch
    
    #Método estático que retorna a sessão válida que possue determinada unidade
    @staticmethod
    def pegaPorUnidade(unidade):
        #Retorna a sessão válida correspondente
        fetch = dao.SessaoDAO.pegarPorUnidade(unidade)
        return fetch[0][1]

#Classe que operacionaliza as funções do agendamento
class agendamentoControle:
    #Instancia o Modelo
    #Instancia o DAO
    def __init__(self):
        self.agendamento = model.Agendamento()
        self.agendamentoDAO = dao.AgendamentoDAO()

    #Realiza a tentativa de agendamento
    def registrar_agendamento(self, fk_id_aluno, fk_id_sessao):
        #Seta os atributos necessários para realizar o agendamento
        self.agendamento.set_statusAgendamento("Válido")
        self.agendamento.set_fk_id_aluno(fk_id_aluno)
        self.agendamento.set_fk_id_sessao(fk_id_sessao)
        #Encapsula o id do agendamento obtido dentro de userId
        #Por padrão todos os id's são inicializados como -1
        #Portanto, caso o id seja menor que 0, significa que não gouve o cadastro
        userId = self.agendamentoDAO.inserir(self.agendamento)
        if(userId > 0):
            #Seta o id do agendamento
            self.agendamento.set_id_agendamento = userId
            return True
        else:
            #Retorna false, criar exceção
            return False
    
    #Método estático que retorna a sessão válida e utiliza como parâmetro o id_aluno
    @staticmethod
    def pegarValidaPorId(id_aluno):
        #Chama a função estática que realiza a busca
        return dao.AgendamentoDAO.pegarValidaPorId(id_aluno)
    
    @staticmethod
    def invalidaStatus(id_aluno, id_sessao):
        return dao.AgendamentoDAO.invalidaStatus(id_aluno, id_sessao)
    
    #Método estático busca todos os agendamentos de determinado id_aluno
    @staticmethod
    def pegarPorId(id_aluno):
        #Método DAO que fala com o banco
        return dao.AgendamentoDAO.pegarPorId(id_aluno)

#Classe que operacionaliza as funções do operador
class operadorControle:
    #Instancia o Modelo
    #Intancia o DAO
    def __init__(self):
        self.operador = model.Operador()
        self.operadorDAO = dao.OperadorDAO()

    #Checa se o login do operador é valido
    def login_operador(self, identificador, senha):
        #Seta os atributos necessários para o login
        self.operador.set_cpf(identificador)
        self.operador.set_senha(senha)
        #tenta realizar o login
        fetch = self.operadorDAO.efetuarLogin(self.operador)
        #Caso não haja retorno 
        if not fetch:
            return None 
        #Caso o login exista
        else:
            #seta os atributos do operador
            self.operador.set_id_operador(fetch[0][0])
            self.operador.set_nome(fetch[0][1])
            self.operador.set_cpf(fetch[0][2])
            self.operador.set_telefone(fetch[0][3])
            self.operador.set_email(fetch[0][4])
            self.operador.set_senha(fetch[0][5])
            self.operador.set_unidade(fetch[0][6])
            #retorna o modelo do operador
            return self.operador

class atendimentoControle():
    def __init__(self):
        self.atendimento = model.Atendimento()
        self.atendimentoDAO = dao.AtendimentoDAO()

    def validaAgendamento():
        pass
    
    #Func que tenta realizar o registro de atendimento
    def registrar_atendimento(self, tipoAtendimento, fk_id_aluno, fk_id_sessao, id_operador):
        #Seta os atributos necessários para o registro
        self.atendimento.set_tipoAtendimento(tipoAtendimento)
        self.atendimento.set_fk_id_aluno(fk_id_aluno)
        self.atendimento.set_fk_id_sessao(fk_id_sessao)
        self.atendimento.set_fk_id_operador(id_operador)
        #Inser o id do atendimento realizando dentro de UserID
        userId = self.atendimentoDAO.inserir(self.atendimento)
        #Por padrão o id é setado como -1, logo caso ele não seja maior que 0, significa que o registro nao aconteceu
        if(userId > 0):
            #Seta o id_atendimento
            self.atendimento.set_id_atendimento = userId
            #Casp atendimento 1, fecha o status do agendamento
            if(tipoAtendimento == '1'):
                dao.AgendamentoDAO.invalidaStatus(fk_id_aluno, fk_id_sessao)
            return True
        else:
            #adicionar exceção, pois como else não funciona
            return False
    #Método estático que busca os atendimentos por operador
    @staticmethod
    def pegarPorOperador(id_operador):
        #Retorna os atendimentos realizados pelo operador
        return dao.AtendimentoDAO.pegarPorOperador(id_operador)

