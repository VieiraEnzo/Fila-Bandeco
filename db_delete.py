import sqlite3

conn = sqlite3.connect('filaRU.db') 
c = conn.cursor()

c.execute("DELETE from aluno where nome <> ''")      
                     
conn.commit()