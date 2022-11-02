import sqlite3

conn = sqlite3.connect('../filaRU.db')
c = conn.cursor()

#j = c.execute("select id_sessao, dtInicioSessao, dtFimSessao, statusSessao, cardapio, unidade from sessao inner join refeicao on sessao.fk_id_refeicao = refeicao.id_refeicao").fetchall()
j = c.execute("select * from aluno").fetchall()
conn.commit()

print(j)