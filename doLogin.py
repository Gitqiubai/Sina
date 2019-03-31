import requests
from SinaSpider.severdata import reData
import demjson
import os
from Sina.doModle import getMessage,addDlog,addComment,addFab
import rsa
import binascii
import math
import random
import time
import base64
from Sina.Data import reDuanzi
from Sina.doModle import getHost,getMblog,getUid
from multiprocessing import Pool,Process



CList=["MTMxOTc2Njc2ODE=","NDM4NzkzOTU3JTQwcXEuY29t","MTM0NzE5NDk0Nzk="]

#idBox={'uid':5415830208,'mid':4265474784844012,'content':'该睡觉了。0'}

#---------选择需要测试的账号---------
#su="NDM4NzkzOTU3JTQwcXEuY29t"  #438

#---------选择需要测试的账号---------

loginurl='https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'

def get_password(password, servertime, nonce, pubkey):
    rsa_publickey = int(pubkey, 16)
    key = rsa.PublicKey(rsa_publickey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    message = message.encode("utf-8")
    passwd = rsa.encrypt(message, key)
    passwd = binascii.b2a_hex(passwd)
    return passwd.decode('utf8')


def getServerData(su,passw,proxy):
    count=base64.b64encode(su.encode('utf8')).decode('utf8')
    cok = requests.session()
    header={
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://weibo.com",
                "Referer": "https://weibo.com/",
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
            }
    prama = {
        "entry": "weibo",
        "callback": "sinaSSOController.preloginCallBack",
        "su": count,
        "rsakt": "mod",
        "checkpin": "1",
        "client": "ssologin.js(v1.4.19)"
    }
    url = 'https://login.sina.com.cn/sso/prelogin.php'
    r = requests.get(url, params=prama,proxies=proxy)
    js = r.text.replace('sinaSSOController.preloginCallBack(', '').replace(')', '')
    js = demjson.decode(js)

    #print(js)
    if js['showpin'] == 1 :
        print('此次登录需要验证码')
     
        sp=get_password(passw,js['servertime'],js['nonce'],js["pubkey"])
        #---------请求验证码阶段---------
        parm = {
            "r": math.floor(random.random() * math.pow(10, 8)),
            "s": "0",
            "p": js['pcid']
        }
        randomUrl = 'https://login.sina.com.cn/cgi/pin.php'
        r = requests.get(randomUrl, params=parm,proxies=proxy)
        F = open('验证码.png', 'wb')
        F.write(r.content)
        F.close()
        print('验证码已保存')
        door = input('请输入验证码:')
        #---------请求验证码阶段---------
        postData = {
                        "entry": "weibo",
                        "gateway": "1",
                        "from": "",
                        "savestate": "7",
                        "qrcode_flag": "false",
                        "useticket": "1",
                        "pagerefer": "",
                        "pcid": js['pcid'],
                        "door": door,
                        "vsnf": "1",
                        "su": count,
                        "service": "miniblog",
                        "servertime": js['servertime'],
                        "nonce": js['nonce'],
                        "pwencode": "rsa2",
                        "rsakv": js['rsakv'],
                        "sp": sp,
                        "sr": "1536*864",
                        "encoding": "UTF-8",
                        "cdult": "2",
                        "domain": "weibo.com",
                        "prelt": "34",
                        "returntype": "TEXT"
                    }
        r = cok.post(loginurl, data=postData, headers=header,proxies=proxy)
        retcode = demjson.decode(r.text)

        if retcode['retcode'] != '0':
            print(retcode['retcode'],retcode['reason'])
        #print(retcode['retcode'], retcode['uid'], retcode['nick'])
        else:
            cookies = ''
            for item in cok.cookies.items():
                cookies = cookies + item[0] + '=' + item[1] + ';'
            with open('./cookies/{}.txt'.format(su), 'a') as F:
                F.write(cookies)
                print('UID:【{}】 Name:【{}】 登录成功cookies保存至{}.txt'.format(retcode['uid'], retcode['nick'], su))
                print('-----' * 10)
            # #print(r.text)
            # print('登录成功Cookies为:', r.cookies.get_dict())
            # cookies = ''
            # for item in cok.cookies.items():
            #     cookies = cookies + item[0] + '=' + item[1] + ';'
            # with open('./cookies/{}.txt'.format(su), 'a') as F:
            #     F.write(cookies)
            #     print('带验证码登录成功cookies保存至cookies.txt')
            # retcode = demjson.decode(r.text)
            # print(retcode)


    else:
        print('此次登录不需要验证码')
        sp = get_password(passw, js['servertime'], js['nonce'], js["pubkey"])
        postData = {
                        "entry": "weibo",
                        "gateway": "1",
                        "from": "",
                        "savestate": "7",
                        "qrcode_flag": "false",
                        "useticket": "1",
                        "pagerefer": "http://www.sina.com.cn/",
                        "vsnf": "1",
                        "su": count,
                        "service": "miniblog",
                        "servertime": js['servertime'],
                        "nonce": js['nonce'],
                        "pwencode": "rsa2",
                        "rsakv": js['rsakv'],
                        "sp": sp,
                        "sr": "1536*864",
                        "encoding": "UTF-8",
                        "cdult": "2",
                        "domain": "weibo.com",
                        "prelt": "39",
                        "returntype": "TEXT"
                    }
        r = cok.post(loginurl, data=postData, headers=header,proxies=proxy)
        retcode = demjson.decode(r.text)
        if retcode['retcode'] != '0':
            print(retcode['retcode'],retcode['reason'])
        #print(retcode['retcode'], retcode['uid'], retcode['nick'])
        else:

            cookies = ''
            for item in cok.cookies.items():
                cookies = cookies + item[0] + '=' + item[1] + ';'
            with open('./cookies/{}.txt'.format(su), 'a') as F:
                F.write(cookies)
                print('UID:【{}】 Name:【{}】 登录成功cookies保存至{}.txt'.format(retcode['uid'],retcode['nick'],su))
                print('-----' * 10)


def login(su,passw,Proxies):
    proxy = Proxies[random.randint(0, len(Proxies) - 1)]
    #print(os.path.exists("./cookies/{}.txt".format(su)))
    if os.path.exists("./cookies/{}.txt".format(su)):
        print('-----'*10)
        print('账号【{}】已存在cookies可直接进行登录'.format(su))
        F = open('./cookies/{}.txt'.format(su), 'r')
        cookies = F.read()
        F.close()
        #获取个人信息
        contents=reDuanzi.reText()
        #print(contents)
        uid=getUid(cookies,proxy)
        print('uid={}'.format(uid))
        while True:
            #if 1:
            try:
                for i in range(random.randint(2,3)):
                    rand = random.randint(0,3)
                    if rand == 0:
                        getHost(cookies, proxy, su)
                    if rand == 1:
                        getMblog(su, cookies, proxy, uid)
                        #pass
                    if rand == 2:
                        ran=random.randint(3,4)
                        print('什么也不做就等{}s'.format(ran))
                        time.sleep(ran)
                    if ran == 3:
                        content = contents[random.randint(0, len(contents) - 1)][0]
                        addDlog(cookies, content, proxy,su)
                    time.sleep(random.randint(2,6))
                # print('测试')
                # getMblog(su,cookies,proxy,uid)


                #getMessage(cookies,proxy)
                #评论
                #addComment(cookies,idBox['content'],idBox['uid'],idBox['mid'],proxy)
                #发布微博
                #content=contents[random.randint(0,len(contents)-1)][0]
                #addDlog(cookies,content,proxy)
                #点赞
                #addFab(cookies,idBox['mid'],proxy)
                #转发
                #getHost(cookies,proxy,su)
                #time.sleep(random.randint(5,12))
                break
            #else:
            except:
                #print('切换代理ip')
                proxy = Proxies[random.randint(0, len(Proxies) - 1)]
                print('【{}】切换代理【{}】'.format(su,proxy))
                #break

    else:
        print('-----' * 10)
        print('账号：{} 的cookies不存在'.format(su))
        print('账号：{}进行登录'.format(su))
        getServerData(su,passw,proxy)


