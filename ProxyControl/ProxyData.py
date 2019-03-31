import sqlite3




def ReProxy():
    con = sqlite3.connect('Proxy.db')
    cursor = con.cursor()
    cursor.execute('create table  if not exists ProxyList(id INTEGER primary key autoincrement,type varchar(50),ip varchar(100) )')
    data=cursor.execute('select * from ProxyList').fetchall()
    con.commit()
    cursor.close()
    con.close()
    List=[]
    for each in data:
        List.append({each[1]:each[2]})
    #print(List)
    return List
    #print(data)

#ReProxy()