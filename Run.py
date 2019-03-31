from Sina.doLogin import login
import demjson
from multiprocessing import Process,Pool
from Sina.ProxyControl import ProxyData
import random
import sqlite3
import requests
from Sina.doModle import getHost


# a=ProxyData.ReProxy()
# print(a)


if __name__ == "__main__":
    Proxies = ProxyData.ReProxy()
    #proxy = Proxies[random.randint(0, len(Proxies) - 1)]
   #proxy = {"http": "http://111.230.129.13:11233"}
    F = open('count.txt', 'r')
    db = F.read()
    F.close()
    DB = demjson.decode(db)
    print(DB)
    p=Pool(2)

    for each in DB:
        #print(len(proxies))
        #proxy=proxies[random.randint(0,len(proxies))]
        p.apply_async(login,args=(each,DB[each],Proxies,))
        #p.apply_async(getHost,args=(each,DB[each],Proxies,))
        #print(proxy)
    p.close()
    p.join()
    print('多进程运行结束')

#
def dologin():
    Proxies = ProxyData.ReProxy()
    #proxy = Proxies[random.randint(0, len(Proxies) - 1)]
   #proxy = {"http": "http://111.230.129.13:11233"}
    F = open('count.txt', 'r')
    db = F.read()
    F.close()
    DB = demjson.decode(db)
    print(DB)

    for each in DB:
        #print(len(proxies))
        #proxy=proxies[random.randint(0,len(proxies))]
        login(each,DB[each],Proxies)
        #p.apply_async(login,args=(each,DB[each],Proxies,))
        #print(proxy)

    print('多进程运行结束')


dologin()