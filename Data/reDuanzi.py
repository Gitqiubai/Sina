import sqlite3
from random import randint

def reText():
    con=sqlite3.connect('duanZi.db')
    cursor=con.cursor()
    #cursor.execute('create table if not exists tables (id INTEGER primary key autoincrement,content text )')
    duanzi=cursor.execute('select content from tables').fetchall()
    return duanzi

#text=reText()
#print(text[randint(0,len(text))][0])
