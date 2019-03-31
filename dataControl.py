import sqlite3
import random
import telnetlib



db=sqlite3.connect('test.db')


def reProxy():
    cursor = db.cursor()
    cursor.execute("create table if not exists ipoll (id INTEGER primary key autoincrement,type varchar(50),address varchar(100),port varchar(50),ban BOOLEAN)")

    while True:
        try:
            cursor.execute("select * from ipoll where ban={}".format(0))
            data = cursor.fetchall()
            randomData = data[random.randint(0, len(data) - 1)]

            try:
                telnetlib.Telnet(randomData[2], port=randomData[3], timeout=20)
                print('此ip可用{}'.format(randomData[2]))
                return {randomData[1]:"{}://{}:{}".format(randomData[1],randomData[2],randomData[3])}
                break
            except:
                print('测试代理失败')
                cursor.execute('update ipoll set ban=1 where id={}'.format(randomData[0]))
                db.commit()
        except:
            print('代理链接全不可用')
            break

    cursor.close()
    db.commit()
    db.close()
reProxy()
