class Aluno:

    def __init__(self, id_aluno, nome, cpf, telefone, email, senha, dre):
        self,id_aluno
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.dre = dre
    
class Atendimento:

    def __init__(self, id_atendimento, dtAtendimento, tipoAtendimento, fk_id_aluno, fk_id_operator, fk_id_sessao):
        self.id_atendimento = id_atendimento
        self.dtAtendimento = dtAtendimento
        self.tipoAtendimento = tipoAtendimento
        self.fk_id_aluno = fk_id_aluno
        self.fk_id_operator = fk_id_operator
        self.fk_id_sessao = fk_id_sessao


class Operador:

    def __init__(self, id_operador, nome, cpf, telefone, email, senha, dtPrimeiroCadastro, unidade):
        self.id_operador = id_operador
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.dtPrimeiroCadastro = dtPrimeiroCadastro
        self.unidade = unidade


class Administrador:

    def __init__(self, id_administrador, nome, cpf, telefone, email, senha, dtPrimeiroCadastro, siape):
        self.id_administrador = id_administrador
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.dtPrimeiroCadastro = dtPrimeiroCadastro
        self.siape = siape


class Agendamento:

    def __init__(self, id_agendamento, dtAgendamento, dtAgendada, statusAgendamento, fk_id_aluno, fk_id_sessao):
        self.id_agendamento = id_agendamento
        self.dtAgendamento = dtAgendamento
        self.dtAgendada = dtAgendada
        self.statusAgendamento = statusAgendamento
        self.fk_id_aluno = fk_id_aluno
        self.fk_id_sessao = fk_id_sessao


class Sessao:

    def __init__ (self, id_sessao, dtCadastroSessao, statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao):
        self.id_sessao = id_sessao
        self.dtCadastroSessao = dtCadastroSessao
        self.statusSessao = statusSessao
        self.dtInicioSessao = dtInicioSessao
        self.dtFimSessao = dtFimSessao
        self.fk_id_refeicao = fk_id_refeicao


class Refeicao:

    def __init__(self,  id_refeicao, cardapio, statusRefeicao, dtInicoRefeicao, dtFimRefeicao, dtCadastroRefeicao, fk_id_administrador):
        self.id_refeicao = id_refeicao
        self.cardapio = cardapio
        self.statusrefeicao = statusRefeicao
        self.dtInicioRefeicao = dtInicoRefeicao
        self.dtFimRefeicao =dtFimRefeicao
        self.dtCadastroRefeicao = dtCadastroRefeicao
        self.fk_id_administrador = fk_id_administrador