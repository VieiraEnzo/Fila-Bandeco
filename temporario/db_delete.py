import sqlite3

conn = sqlite3.connect('filaRU.db') 
c = conn.cursor()
    

c.execute('''
        CREATE TABLE aluno (
            id_aluno INTEGER primary key AUTOINCREMENT,
            nome varchar(200),
            cpf varchar(200),
            telefone varchar(200),
            email varchar(200),
            senha varchar(200),
            dtPrimeiroCadastro timestamp default current_timestamp not null,
            dre varchar(200) not null unique
        );
          ''')
        
conn.commit()