import sqlite3

conn = sqlite3.connect('filaRU.db') 
c = conn.cursor()
    
c.execute('''
        drop table sessao;
          ''')

conn.commit()