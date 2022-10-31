import sqlite3

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE aluno (
            id_aluno INTEGER AUTOINCREMENT primary key,
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
            id_operador serial primary key,
            nome varchar(200),
            cpf varchar(200),
            telefone varchar(200),
            email varchar(200),
            senhar varchar(200),
            dtPrimeiroCadastro timestamp default current_timestamp not null,
            unidade varchar(1)
        );
          ''')

c.execute('''
        CREATE TABLE administrador (
            id_administrador serial primary key,
            nome varchar(200),
            cpf varchar(200),
            telefone varchar(200),
            email varchar(200),
            senhar varchar(200),
            dtPrimeiroCadastro timestamp default current_timestamp not null,
            siape varchar(200) not null unique
        );
          ''')

c.execute('''
        CREATE TABLE refeicao(
            id_refeicao serial primary key,
            cardapio varchar(200),
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
            id_sessao serial primary key,
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
            id_atendimento serial primary key,
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
            id_agendamento serial primary key,
            dtAgendamento timestamp default current_timestamp not null,
            dtAgendada datetime,
            statusAgendamento varchar(200),
            fk_id_aluno bigint unsigned not null,
            fk_id_sessao bigint unsigned not null,
            foreign key (fk_id_sessao) references sessao (id_sessao),
            foreign key (fk_id_aluno) references aluno (id_aluno)
        );
          ''')
          
                     
conn.commit()