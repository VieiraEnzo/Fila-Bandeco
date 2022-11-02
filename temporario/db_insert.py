import sqlite3

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

nome = "Teste2"
cpf = "Teste2"
telefone = "Teste2"
email = "Teste2"
senha = "Teste2"
dre = "Teste2"

#c.execute("insert into aluno (nome, cpf, telefone, email, senha, dre) values (?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, email, senha, dre))

#c.execute("insert into administrador (nome, cpf, telefone, email, senha, siape) values ('Ana', '88888888888', '99999999', 'ana@ufrj.br', '123', '123456789')")

#c.execute("insert into refeicao (cardapio, unidade, statusRefeicao, dtInicioRefeicao, dtFimRefeicao, fk_id_administrador) values ('Brocolis', 'Letras', 'Aberta', '2022-11-1 11:30:00', '2022-11-1 14:30:00', '1')")

#c.execute("insert into sessao (statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao) values ('Válida', '2022-11-1 13:30:00', '2022-11-1 14:30:00', 3)")

#c.execute("insert into sessao (statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao) values ('Válida', '2022-11-1 11:30:00', '2022-11-1 12:30:00', 3)")

#c.execute("insert into sessao (statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao) values ('Válida', '2022-11-1 12:30:00', '2022-11-1 13:30:00', 3)")

conn.commit()