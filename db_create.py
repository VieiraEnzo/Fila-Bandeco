import sqlite3

#Tabelas utilizadas na construção do sistema
#Não existe uma interface de CRUD para o admnistrador, refeição e sessão, pois não houve tempo suficiente, logo eles foram instanciados manualmente

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE aluno (
            id_aluno INTEGER AUTO_INCREMENT primary key,
            nome varchar(200),
            cpf varchar(200),
            telefone varchar(200),
            email varchar(200),
            senha varchar(200),
            dtPrimeiroCadastro timestamp default current_timestamp not null,
            dre varchar(200) not null unique
        );
          ''')

c.execute('''
        CREATE TABLE operador (
            id_operador INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(200),
            cpf varchar(200),
            telefone varchar(200),
            email varchar(200),
            senha varchar(200),
            unidade varchar(200),
            dtPrimeiroCadastro timestamp default current_timestamp not null
        );
          ''')

c.execute('''
        CREATE TABLE administrador (
            id_administrador INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(200),
            cpf varchar(200),
            telefone varchar(200),
            email varchar(200),
            senha varchar(200),
            dtPrimeiroCadastro timestamp default current_timestamp not null,
            siape varchar(200) not null unique
        );
          ''')

c.execute('''
        CREATE TABLE refeicao(
            id_refeicao INTEGER PRIMARY KEY AUTOINCREMENT,
            cardapio varchar(200),
            unidade varchar(200),
            statusRefeicao varchar(200),
            dtInicioRefeicao datetime,
            dtFimRefeicao datetime,
            dtCadastroRefeicao timestamp default current_timestamp not null,
            fk_id_administrador bigint unsigned not null,
            foreign key (fk_id_administrador) references administrador (id_administrador)
        );
          ''')

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

c.execute('''
        CREATE TABLE agendamento(
            id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
            dtAgendamento timestamp default current_timestamp not null,
            statusAgendamento varchar(200),
            fk_id_aluno bigint unsigned not null,
            fk_id_sessao bigint unsigned not null,
            foreign key (fk_id_sessao) references sessao (id_sessao),
            foreign key (fk_id_aluno) references aluno (id_aluno)
        );
          ''')
          
                     
conn.commit()