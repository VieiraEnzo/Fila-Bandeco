import sqlite3

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

nome = "Teste2"
cpf = "Teste2"
telefone = "Teste2"
email = "Teste2"
senha = "Teste2"
dre = "Teste2"

c.execute("insert into aluno (nome, cpf, telefone, email, senha, dre) values (?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, email, senha, dre))
j = c.execute("select last_insert_rowid()").fetchall()
conn.commit()

print(j[0][0])