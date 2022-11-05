import sqlite3

conn = sqlite3.connect('filaRU.db', check_same_thread=False)
c = conn.cursor()

class AlunoDAO:
    #Insere no banco de dados
    def inserir(self, aluno):
        c.execute("insert into aluno (nome, cpf, telefone, email, senha, dre) values (?, ?, ?, ?, ?, ?)", (aluno.get_nome(), aluno.get_cpf(), aluno.get_telefone(), aluno.get_email(), aluno.get_senha(), aluno.get_dre()))
        #Pega o último ID inserido, ainda na mesma instancia do banco de dados
        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()
        #Retorna o id
        return userId[0][0]
    
    #Verifica se os atributos setados correspondem a algum cadastro
    def efetuarLogin(self, aluno):
        fetch = c.execute("select * from aluno where cpf = ? and senha = ? ", (aluno.get_cpf(), aluno.get_senha())).fetchall()
        conn.commit()
        #Retorna a linha encontrada pela query, não retorna mais de uma linha pois o cadastro possui campos únicos
        return fetch

    #Método estático que busca um aluno através do CPF
    @staticmethod
    def pegarPorCpf(cpf):
        fetch = c.execute("select id_aluno from aluno where cpf = ?", (cpf,)).fetchall()
        conn.commit()

        return fetch

class SessaoDAO:
    @staticmethod
    def pegarTodos():
        fetch = c.execute("select id_sessao, dtInicioSessao, dtFimSessao, statusSessao, cardapio, unidade from sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao").fetchall()

        conn.commit()

        return fetch
    
    #Método estático que retorna a sessão e utiliza como chave a unidade
    @staticmethod
    def pegarPorUnidade(unidade):
        fetch = c.execute("select id_sessao, id_refeicao from sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao where unidade = ? and statusSessao = 'Válida'", (unidade,)).fetchall()
        conn.commit()

        return fetch


class AgendamentoDAO:
    #tenta realizar um agendamento
    def inserir(self, agendamento):
        c.execute("insert into agendamento (statusAgendamento, fk_id_aluno, fk_id_sessao) values (?, ?, ?)", (agendamento.get_statusAgendamento(), agendamento.get_fk_id_aluno(), agendamento.get_fk_id_sessao()))
        #Insere o id recebi dentro de userId
        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()
        #Retorna o ID
        return userId[0][0]

    #Método estático que busca a sessão válida realizando inner join's 
    @staticmethod
    def pegarValidaPorId(id_aluno):
        #Como o agendamento cria relação com o aluno e a sessão, está lógica é utilizada para buscar a sessão válida que possui o agendamento
        fetch = c.execute("select id_agendamento, id_refeicao, id_sessao from agendamento inner join sessao on agendamento.fk_id_sessao = sessao.id_sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao where fk_id_aluno = ? and statusSessao = 'Válida' order by id_agendamento desc limit 1", (id_aluno,)).fetchall()
        conn.commit()

        return fetch[0][2]

    #Método estático que fecha o status do agendamento
    @staticmethod
    def invalidaStatus(id_aluno, id_sessao):
        c.execute("update agendamento set statusAgendamento = 'Fechado' where fk_id_aluno = ? and fk_id_sessao = ?", (id_aluno, id_sessao,)).fetchall()
        conn.commit()

    #Método estático que busca agendamento e utiliza como chame o id_aluno
    @staticmethod
    def pegarPorId(id_aluno):
        fetch = c.execute("select * from agendamento where fk_id_aluno = ?", (id_aluno,)).fetchall()
        conn.commit()
        #Retorna uma lista de agendamentos
        return fetch

class OperadorDAO:
    #Busca por um registro com as informações obtidas
    def efetuarLogin(self, operador):
        fetch = c.execute("select * from operador where cpf = ? and senha = ? ", (operador.get_cpf(), operador.get_senha())).fetchall()
        conn.commit()
        #Retorna o resultado obtido
        return fetch

#Classe que insere o atendimento no banco de dados
class AtendimentoDAO:
    def inserir(self, atendimento):
        c.execute("insert into atendimento (tipoAtendimento, fk_id_aluno, fk_id_operador, fk_id_sessao) values (?, ?, ?, ?)", (atendimento.get_tipoAtendimento(), atendimento.get_fk_id_aluno(), atendimento.get_fk_id_operador(), atendimento.get_fk_id_sessao()))
        #Retorna o id do atendimento cadastrado
        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()

        return userId[0][0]
    
    #Busca por registros de atendimentos efetuados por determinado operador
    def pegarPorOperador(id_operador):
        fetch = c.execute("select nome, dtAtendimento, tipoAtendimento from atendimento inner join aluno on atendimento.fk_id_aluno = aluno.id_aluno where fk_id_operador = ?", (id_operador,)).fetchall()
        conn.commit()
        #Retorna os registros encontrados
        return fetch
