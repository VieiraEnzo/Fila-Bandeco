import sqlite3

conn = sqlite3.connect('filaRU.db') 
c = conn.cursor()
    

c.execute('''
        CREATE TABLE sessao(
            id_sessao INTEGER PRIMARY KEY AUTOINCREMENT,
            dtCadastroSessao timestamp default current_timestamp not null,
            statusSessao varchar(200),
            dtInicioSessao datetime,
            dtFimSessao datetime,
            fk_id_refeicao bigint unsigned not null,
            foreign key (fk_id_refeicao) references refeicao (id_refeicao)
        );
          ''')


conn.commit()