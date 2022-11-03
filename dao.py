import sqlite3

conn = sqlite3.connect('filaRU.db', check_same_thread=False)
c = conn.cursor()

class AlunoDAO:
    def inserir(self, aluno):
        c.execute("insert into aluno (nome, cpf, telefone, email, senha, dre) values (?, ?, ?, ?, ?, ?)", (aluno.get_nome(), aluno.get_cpf(), aluno.get_telefone(), aluno.get_email(), aluno.get_senha(), aluno.get_dre()))

        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()

        return userId[0][0]
    
    def efetuarLogin(self, aluno):
        fetch = c.execute("select * from aluno where cpf = ? and senha = ? ", (aluno.get_cpf(), aluno.get_senha())).fetchall()
        conn.commit()

        return fetch

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
    
    @staticmethod
    def pegarPorUnidade(unidade):
        fetch = c.execute("select id_sessao, id_refeicao from sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao where unidade = ? and statusSessao = 'Válida'", (unidade,)).fetchall()
        conn.commit()

        return fetch

class AgendamentoDAO:
    def inserir(self, agendamento):
        c.execute("insert into agendamento (statusAgendamento, fk_id_aluno, fk_id_sessao) values (?, ?, ?)", (agendamento.get_statusAgendamento(), agendamento.get_fk_id_aluno(), agendamento.get_fk_id_sessao()))

        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()

        return userId[0][0]

    @staticmethod
    def pegarValidaPorId(id_aluno):
        fetch = c.execute("select id_agendamento, id_refeicao, id_sessao from agendamento inner join sessao on agendamento.fk_id_sessao = sessao.id_sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao where fk_id_aluno = ? and statusSessao = 'Válida' order by id_agendamento desc limit 1", (id_aluno,)).fetchall()
        conn.commit()

        return fetch[0][2]

    @staticmethod
    def invalidaStatus(id_aluno, id_sessao):
        c.execute("update agendamento set statusAgendamento = 'Fechado' where fk_id_aluno = ? and fk_id_sessao = ?", (id_aluno, id_sessao,)).fetchall()
        conn.commit()

    @staticmethod
    def pegarPorId(id_aluno):
        fetch = c.execute("select * from agendamento where fk_id_aluno = ?", (id_aluno,)).fetchall()
        conn.commit()

        return fetch

class OperadorDAO:
    def efetuarLogin(self, operador):
        fetch = c.execute("select * from operador where cpf = ? and senha = ? ", (operador.get_cpf(), operador.get_senha())).fetchall()
        conn.commit()

        print(fetch)
        return fetch

class AtendimentoDAO:
    def validaAgendamento(self, operador):
        pass
    
    def inserir(self, atendimento):
        c.execute("insert into atendimento (tipoAtendimento, fk_id_aluno, fk_id_operador, fk_id_sessao) values (?, ?, ?, ?)", (atendimento.get_tipoAtendimento(), atendimento.get_fk_id_aluno(), atendimento.get_fk_id_operador(), atendimento.get_fk_id_sessao()))

        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()

        return userId[0][0]
    
    def pegarPorOperador(id_operador):
        fetch = c.execute("select nome, dtAtendimento, tipoAtendimento from atendimento inner join aluno on atendimento.fk_id_aluno = aluno.id_aluno where fk_id_operador = ?", (id_operador,)).fetchall()
        conn.commit()

        return fetch
