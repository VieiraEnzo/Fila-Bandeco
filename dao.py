import sqlite3

conn = sqlite3.connect('filaRU.db', check_same_thread=False)
c = conn.cursor()

class AlunoDAO:
    def inserir(self, aluno):
        c.execute("insert into aluno (nome, cpf, telefone, email, senha, dre) values (?, ?, ?, ?, ?, ?)", (aluno.get_nome(), aluno.get_cpf(), aluno.get_telefone(), aluno.get_email(), aluno.get_senha(), aluno.get_dre()))

        userId = c.execute("select last_insert_rowid()").fetchall()

        conn.commit()

        return userId[0][0]
        