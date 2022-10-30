import sqlite3

conn = sqlite3.connect('filaRU.db')
c = conn.cursor()

j = c.execute("select * from aluno").fetchall()
conn.commit()

print(j)