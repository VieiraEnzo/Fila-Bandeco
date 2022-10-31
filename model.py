class Aluno:

    def __init__(self):
        self.__id_aluno = None
        self.__nome = None
        self.__cpf = None
        self.__telefone = None
        self.__email = None
        self.__senha = None
        self.__dre = None
        self.__dtPrimeiroCadastro = None

    def set_id_aluno(self, var):
        self.__id_aluno = var

    def get_id_aluno(self):
        return self.__id_aluno
    
    def set_nome(self, var):
        self.__nome = var

    def get_nome(self):
        return self.__nome

    def set_cpf(self, var):
        self.__cpf = var

    def get_cpf(self):
        return self.__cpf

    def set_telefone(self, var):
        self.__telefone = var

    def get_telefone(self):
        return self.__telefone

    def set_email(self, var):
        self.__email = var

    def get_email(self):
        return self.__email
    
    def set_senha(self, var):
        self.__senha = var

    def get_senha(self):
        return self.__senha
    
    def set_dre(self, var):
        self.__dre = var

    def get_dre(self):
        return self.__dre
    
    
class Atendimento:

    def __init__(self, id_atendimento, dtAtendimento, tipoAtendimento, fk_id_aluno, fk_id_operator, fk_id_sessao):
        self.__id_atendimento = id_atendimento
        self.__dtAtendimento = dtAtendimento
        self.__tipoAtendimento = tipoAtendimento
        self.__fk_id_aluno = fk_id_aluno
        self.__fk_id_operator = fk_id_operator
        self.__fk_id_sessao = fk_id_sessao

    def set_id_atendimento(self, var):
        self.__id_atendimento = var

    def get_id_atendimento(self):
        return self.__id_atendimento
    
    def set_tipoAtendimento(self, var):
        self.__tipoAtendimento = var

    def get_tipoAtendimento(self):
        return self.__tipoAtendimento

    def set_fk_id_aluno(self, var):
        self.__fk_id_aluno = var

    def get_fk_id_aluno(self):
        return self.__fk_id_aluno

    def set_fk_id_operator(self, var):
        self.__fk_id_operator = var

    def get_fk_id_operator(self):
        return self.__fk_id_operator
    
    def set_fk_id_sessao(self, var):
        self.__fk_id_sessao = var

    def get_fk_id_sessao(self):
        return self.__fk_id_sessao

class Operador:

    def __init__(self, id_operador, nome, cpf, telefone, email, senha, dtPrimeiroCadastro, unidade):
        self.__id_operador = id_operador
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
        self.__dtPrimeiroCadastro = dtPrimeiroCadastro
        self.__unidade = unidade

    def set_id_operador(self, var):
        self.__id_operador = var

    def get__id_operador(self):
        return self.__id_operador
    
    def set_nome(self, var):
        self.__nome = var

    def get_nome(self):
        return self.__nome

    def set_cpf(self, var):
        self.__cpf = var

    def get_cpf(self):
        return self.__cpf

    def set_telefone(self, var):
        self.__telefone = var

    def get_telefone(self):
        return self.__telefone

    def set_email(self, var):
        self.__email = var

    def get_email(self):
        return self.__email
    
    def set_senha(self, var):
        self.__senha = var

    def get_senha(self):
        return self.__senha

    def set_unidade(self, var):
        self.__senha = var

    def get_unidade(self):
        return self.__unidade
class Administrador:

    def __init__(self, id_administrador, nome, cpf, telefone, email, senha, dtPrimeiroCadastro, siape):
        self.__id_administrador = id_administrador
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
        self.__dtPrimeiroCadastro = dtPrimeiroCadastro
        self.__siape = siape

    def set_id_administrador(self, var):
        self.__id_administrador = var

    def get_id_administrador(self):
        return self.__id_administrador
    
    def set_nome(self, var):
        self.__nome = var

    def get_nome(self):
        return self.__nome

    def set_cpf(self, var):
        self.__cpf = var

    def get_cpf(self):
        return self.__cpf

    def set_telefone(self, var):
        self.__telefone = var

    def get_telefone(self):
        return self.__telefone

    def set_email(self, var):
        self.__email = var

    def get_email(self):
        return self.__email
    
    def set_senha(self, var):
        self.__senha = var

    def get_senha(self):
        return self.__senha

    def set_siape(self, var):
        self.__siape = var

    def get_siape(self):
        return self.__siape


class Agendamento:

    def __init__(self, id_agendamento, dtAgendamento, dtAgendada, statusAgendamento, fk_id_aluno, fk_id_sessao):
        self.__id_agendamento = id_agendamento
        self.__dtAgendamento = dtAgendamento
        self.__dtAgendada = dtAgendada
        self.__statusAgendamento = statusAgendamento
        self.__fk_id_aluno = fk_id_aluno
        self.__fk_id_sessao = fk_id_sessao

    def set_id_agendamento(self, var):
        self.__id_agendamento = var

    def get_id_agendamento(self):
        return self.__id_agendamento
    
    def set_statusAgendamento(self, var):
        self.__statusAgendamento = var

    def get_statusAgendamento(self):
        return self.__statusAgendamento
    
    def set_fk_id_aluno(self, var):
        self.__fk_id_aluno = var

    def get_fk_id_aluno(self):
        return self.__fk_id_aluno
    
    def set_fk_id_sessao(self, var):
        self.__fk_id_sessao = var

    def get_fk_id_sessao(self):
        return self.__fk_id_sessao

    
class Sessao:

    def __init__ (self, id_sessao, dtCadastroSessao, statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao):
        self.__id_sessao = id_sessao
        self.__dtCadastroSessao = dtCadastroSessao
        self.__statusSessao = statusSessao
        self.__dtInicioSessao = dtInicioSessao
        self.__dtFimSessao = dtFimSessao
        self.__fk_id_refeicao = fk_id_refeicao

    def set_id_sessao(self, var):
        self.__id__sessao = var

    def get_id_sessao(self):
        return self.__id_sessao
    
    def set_statusSessap(self, var):
        self.__statusSessao = var

    def get_statusSessao(self):
        return self.__statusSessao
    
    def set_fk_id_refeicao(self,var):
        self.__fk_id_refeicao = var
    
    def get_fk_id_refeicao(self):
        return self.__fk_id_refeicao


class Refeicao:

    def __init__(self,  id_refeicao, cardapio, statusRefeicao, dtInicoRefeicao, dtFimRefeicao, dtCadastroRefeicao, fk_id_administrador):
        self.__id_refeicao = id_refeicao
        self.__cardapio = cardapio
        self.__statusRefeicao = statusRefeicao
        self.__dtInicioRefeicao = dtInicoRefeicao
        self.__dtFimRefeicao =dtFimRefeicao
        self.__dtCadastroRefeicao = dtCadastroRefeicao
        self.__fk_id_administrador = fk_id_administrador

    def set_id_refeicao(self, var):
        self.__id__refeicao = var

    def get_id_refeicao(self):
        return self.__id_refeicao
    
    def set_cardapio(self, var):
        self.__cardapio = var

    def get_cardapio(self):
        return self.__cardapio
    
    def set_statusRefeicao(self,var):
        self.__statusRefeicao = var
    
    def get_statusRefeicao(self):
        return self.__statusRefeicao
    
    def set_fk_id_administrador(self,var):
        self.__fk_id_administrador = var
    
    def get_fk_id_administrador(self):
        return self.__fk_id_administrador
    