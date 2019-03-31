import sqlite3
import requests
from lxml import etree
import demjson


con=sqlite3.connect('duanZi.db')
cursor=con.cursor()
cursor.execute('create table if not exists tables (id INTEGER primary key autoincrement,content text )')



def getPage(url):
    try:
        #url='http://duanziwang.com/category/%E4%B8%80%E5%8F%A5%E8%AF%9D%E6%AE%B5%E5%AD%90/1/'
        r=requests.get(url)
        r.raise_for_status()
        print('获取【{}】成功'.format(url))
        html=etree.HTML(r.content)
    except:
        print('连接服务器失败')


    #print(html.xpath('//*[@class="post"]/div[1]/h1/a/text()'))
    for each in html.xpath('//*[@class="post"]/div[1]/h1/a/text()'):

        aa=cursor.execute("select * from tables where content='{}'".format(each))
        if len(aa.fetchall()) == 0:
            try:
                cursor.execute('insert into tables (content) values ("{}")'.format(each))
                con.commit()
                print('保存成功')
            except:
                print('错误跳过')
        else:
            pass

def getLink():
    url='http://duanziwang.com/category/%E4%B8%80%E5%8F%A5%E8%AF%9D%E6%AE%B5%E5%AD%90/1/'
    while True:
        r=requests.get(url)
        html=etree.HTML(r.content)
        nextPagr=html.xpath('//*[@class="next"]/@href')
        if len(nextPagr) == 0:
            print('没有下一页了')
            break
        else:
            url=nextPagr[0]
            getPage(url)


getLink()


cursor.close()
con.close()