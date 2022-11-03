import sqlite3

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

nome = "Claudio"
cpf = "Claudio"
telefone = "Claudio"
email = "Claudio"
senha = "Claudio"
unidade = "Central"

c.execute('''
        CREATE TABLE atendimento(
            id_atendimento INTEGER PRIMARY KEY AUTOINCREMENT,
            dtAtendimento timestamp default current_timestamp not null,
            tipoAtendimento varchar(200),
            fk_id_aluno bigint unsigned not null,
            fk_id_operador bigint unsigned not null,
            fk_id_sessao bigint unsigned not null,
            foreign key (fk_id_aluno) references aluno (id_aluno),
            foreign key (fk_id_operador) references operador (id_operador),
            foreign key (fk_id_sessao) references sessao (id_sessao)
        );
          ''')

#c.execute("insert into aluno (nome, cpf, telefone, email, senha, dre) values (?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, email, senha, dre))

#c.execute("insert into operador (nome, cpf, telefone, email, senha, unidade) values (?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, email, senha, unidade))

#c.execute("insert into administrador (nome, cpf, telefone, email, senha, siape) values ('Ana', '88888888888', '99999999', 'ana@ufrj.br', '123', '123456789')")

#c.execute("insert into refeicao (cardapio, unidade, statusRefeicao, dtInicioRefeicao, dtFimRefeicao, fk_id_administrador) values ('Brocolis', 'Letras', 'Aberta', '2022-11-1 11:30:00', '2022-11-1 14:30:00', '1')")

#c.execute("insert into sessao (statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao) values ('Válida', '2022-11-1 13:30:00', '2022-11-1 14:30:00', 3)")

#c.execute("insert into sessao (statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao) values ('Válida', '2022-11-1 11:30:00', '2022-11-1 12:30:00', 3)")

#c.execute("insert into sessao (statusSessao, dtInicioSessao, dtFimSessao, fk_id_refeicao) values ('Válida', '2022-11-1 12:30:00', '2022-11-1 13:30:00', 3)")

conn.commit()