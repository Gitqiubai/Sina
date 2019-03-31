from Sina.doLogin import login
import demjson
from Sina.ProxyControl import ProxyData


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