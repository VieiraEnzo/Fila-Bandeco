import sqlite3

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

#j = c.execute("select id_sessao, dtInicioSessao, dtFimSessao, statusSessao, cardapio, unidade from sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao").fetchall()
#j = c.execute("select * from agendamento inner join aluno on agendamento.fk_id_aluno = aluno.id_aluno").fetchall()

#j = c.execute("select id_agendamento, id_aluno, id_sessao from agendamento inner join sessao on agendamento.fk_id_sessao = sessao.id_sessao inner join aluno on agendamento.fk_id_aluno = aluno.id_aluno;").fetchall()

j = c.execute("select * from agendamento").fetchall()
conn.commit()

print(j)