import sqlite3

conn = sqlite3.connect('filaRU.db') 
c = conn.cursor()
    

c.execute("DROP TABLE administrador")


conn.commit()