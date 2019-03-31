import requests
from lxml import etree
import time
import demjson
import random

#简单的获取个人信息
def getMessage(cookies,proxy):
    cok = requests.session()
    messageIndex = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": cookies,
        "Host": "account.weibo.com",
        "Referer": "https://weibo.com/p/1005053914359348/info?mod=pedit",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
    }
    url2 = 'https://account.weibo.com/set/iframe?skin=skin048'
    messagebox = cok.get(url2, headers=messageIndex,proxies=proxy,timeout=20)
    r=requests.get('http://ip.chinaz.com/getip.aspx',proxies=proxy,timeout=20)
    #print(r.text)
    #print('当前IP为{}'.format(proxy))
    #print(messagebox.text)


    html=etree.HTML(messagebox.content)
    name=html.xpath('//*[@id="pl_content_account"]/div[1]/div[1]/div[2]/div[2]/text()')[0]
    reTime=html.xpath('//*[@id="pl_content_account"]/div[1]/div[1]/div[13]/div[2]/text()')[0]
    #male=html.xpath('//*[@id="pl_content_account"]/div[1]/div[1]/div[5]/div[2]/text()')[0]
    print('--------------------------------------------------\n当前IP为{}\n微博昵称:{}\n注册时间:{}\n--------------------------------------------------'.format(r.text,name,reTime))
    # print('-----' * 10)
    # print('微博昵称:',name)
    # #print('性别:',male)
    # print('注册时间:',reTime)


#微博发布
def addDlog(cookies,content,proxy,su):
    #print('-----------进入发布微博模块---------')
    url='https://weibo.com/aj/mblog/add'
    cok=requests.session()
    postData={
                    "location": "v6_content_home",
                    "text": content,
                    "appkey": "",
                    "style_type": "1",
                    "pic_id": "",
                    "tid": "",
                    "pdetail": "",
                    "mid": "",
                    "isReEdit": "false",
                    "rank": "0",
                    "rankid": "",
                    "module": "stissue",
                    "pub_source": "main_",
                    "pub_type": "dialog",
                    "isPri": "0",
                    "_t": "0"
                }
    header={
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate,br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                #"Content-Length": "250",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie":cookies,
                "Host": "weibo.com",
                "Origin": "https://weibo.com",
                "Referer": "https://weibo.com/u/3914359348/home",
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
    param={
                "ajwvr": "6",
                "__rnd":str(time.time()).replace('.','')[:13]
            }
    r=cok.post(url,params=param,headers=header,data=postData,proxies=proxy)
    #print(r.url)
    #print(demjson.decode(r.content)['code'])
    if demjson.decode(r.content)['code'] == '100000':
        print('【{}】--微博【{}】发布成功！'.format(su,content))
    else:
        print('未知错误,状态码为【{}】'.format(demjson.decode(r.content)['code']))


#评论
def addComment(cookies,content,uid,mid,proxy):
    print('评论：')
    url='https://weibo.com/aj/v6/comment/add'
    cok = requests.session()
    header={
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate,br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                #"Content-Length": "213",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie":cookies,
                "Host": "weibo.com",
                "Origin": "https://weibo.com",
                "Referer": "https://weibo.com/3914359348/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1",
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
    param={
                "ajwvr": "6",
                "__rnd":str(time.time()).replace('.','')[:13]
            }
    postData={
                "act": "post",
                "mid": mid,
                "uid": uid,
                "forward": "0",
                "isroot": "0",
                "content": content,
                "location": "page_100505_home",
                "module": "scommlist",
                "group_source": "",
                "pdetail": "1005053914359348",
                "_t": "0"
            }
    r=cok.post(url,params=param,headers=header,data=postData,proxies=proxy)
    if demjson.decode(r.content)['code'] == '100000':
        print('状态码为【{}】,微博【{}】评论成功！'.format(demjson.decode(r.content)['code'],content))
    else:
        print('未知错误{}'.format(demjson.decode(r.content)['code']))


#点赞
def addFab(cookies,mid,proxy,su,Pageurl,Referer):
    #print('点赞：')
    url = 'https://weibo.com/aj/v6/like/add'
    cok=requests.session()
    param = {
        "ajwvr": "6",
        "__rnd": str(time.time()).replace('.', '')[:13]
    }
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        # "Content-Length": "213",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookies,
        "Host": "weibo.com",
        "Origin": "https://weibo.com",
        "Referer": Referer,
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    postData = {
    "location": "page_100505_home",
    "version": "mini",
    "qid": "heart",
    "mid": mid,
    "loc": "profile",
    "cuslike": "1",
    "_t": "0"
}
    r=cok.post(url,params=param,headers=header,data=postData,proxies=proxy)
    reCOde=demjson.decode(r.content)
    #print(reCOde)
    if demjson.decode(r.content)['code'] == '100000':
        print('【{}】--点赞【{}】成功！--链接【{}】'.format(su,mid,Pageurl))
    else:
        print('未知错误{}'.format(demjson.decode(r.content)['code']))

#转发
def reBlog(mid,referer,proxy,cookies,su,Pageurl):
    resonData=['[doge]','[喵喵]','[二哈]','[跪了]','[允悲]','[思考]','[哆啦A梦微笑]','[哆啦A梦亲亲]']
    reson=resonData[random.randint(0,len(resonData)-1)]
    url='https://weibo.com/aj/v6/mblog/forward'
    rnd = str(time.time()).replace('.', '')[:13]
    postData={
                "pic_src": "",
                "pic_id": "",
                "appkey": "",
                "mid": mid,
                "style_type": "2",
                "mark": "",
                "reason": reson,
                "location": "",
                "pdetail": "",
                "module": "",
                "page_module_id": "",
                "refer_sort": "",
                "is_comment_base": "1",
                "rank": "0",
                "rankid": "",
                "_t": "0"
            }
    parm={
            "ajwvr": "6",
            "domain": "undefined",
            "__rnd": rnd
        }
    head={
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate,br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                "Content-Length": "189",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie":cookies,
                "Host": "weibo.com",
                "Origin": "https://weibo.com",
                "Referer": referer,
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
    r=requests.post(url,headers=head,params=parm,data=postData,proxies=proxy)
    #print(r.text)
    print('【{}】--转发【{}】成功--链接【{}】'.format(su,mid,Pageurl))

def getHost(cookies,proxy,su):

    rnd = str(time.time()).replace('.', '')[:13]
    url = 'https://d.weibo.com/p/aj/discover/loading'
    head = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        #"Cookie": "login_sid_t=be31bfba07dba1fac21c4da7af376e26;cross_origin_proto=SSL;_s_tentry=passport.weibo.com;Apache=7229076204960.079.1533363939224;SINAGLOBAL=7229076204960.079.1533363939224;ULV=1533363939231:1:1:1:7229076204960.079.1533363939224:;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbVQ12Y_zFkFbouHoG8yjr5JpX5K2hUgL.FoqfeoBES0zf1h22dJLoI0qLxKMLBKML12zLxKML1K.LB.BLxKML1K.LB.BLxKML1K.LB.BLxK-LBo5L1hqLxK-L1hqL1-zt;ALF=1564899957;SSOLoginState=1533363958;SCF=AjG1GXVMcFauKX88Is1cZsAZrv1-BoJRYrAVtzo9YkhLT-nqD_lxRqIfGOwpYf5l5wrgSvXRYIANGSG6kqsdO-I.;SUB=_2A252YTamDeRhGeBL6VYT9yzJwz2IHXVVFy9urDV8PUNbmtBeLWn6kW9NRyDzUF8wcGBYExScB__1LLI0CtnRMFjL;SUHB=0LcSGzVr7ZSmTu;un=13197667681;wvr=6;YF-Page-G0=35f114bf8cf2597e9ccbae650418772f;wb_view_log_6524272581=1536*8641.25",
        "Cookie":cookies,
        "Host": "d.weibo.com",
        "Referer": "https://d.weibo.com/623751_1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    parm = {
        "ajwvr": "1",
        "id": "623751_1",
        #"uid": "3914359348",
        "page": "1",
        #"__rnd": rnd
    }
    #==========================================
    time.sleep(random.randint(0,6))
    #==========================================
    r = requests.get(url, headers=head, params=parm,proxies=proxy)
    # req=demjson.decode(r.text)['data']['html']
    #print(r.text)
    html = etree.HTML(demjson.decode(r.text)['data']['html'])
    content = html.xpath('//*[@class="pt_li pt_li_2 S_bg2"]/@href')
    contentLink = []
    for each in content:
        if each[:6] != 'https:':
            contentLink.append('https:' + each)
        else:
            contentLink.append(each)


    head2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie":cookies,
            "Host": "weibo.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
        }
    Pageurl = contentLink[random.randint(0, len(contentLink) - 1)]
    #print(Pageurl)
    r = requests.get(Pageurl, headers=head2,proxies=proxy)
    #print('状态码', r.status_code)
    html = etree.HTML(r.text)
    mid = html.xpath('//*[@id="plc_main"]/div/div/div/div[5]/div/div/@mid')[0]
    #print(mid)
    addFab(cookies,mid,proxy,su,Pageurl)
    time.sleep(random.randint(10, 20))
    reBlog(mid,Pageurl,proxy,cookies,su,Pageurl)

def getUid(cookies,proxy):
    url = 'https://account.weibo.com/set/index'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie":cookies,
        "Host": "account.weibo.com",
        "If-Modified-Since": "Sun,05Aug201814:59:08GMT",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
    }
    param = {
        "topnav": "1",
        "wvr": "6"
    }
    r = requests.get(url, headers=headers, params=param,proxies=proxy)
    html = etree.HTML(r.content)
    data = html.xpath('/html/head/script[1]/text()')[0]
    # print(data)
    D = data.replace('$CONFIG = ', '')
    uid=demjson.decode(D)['uid']
    return uid


def getMblog(su,cookies,proxy,uid):
    Referer="https://weibo.com/u/{}/home?leftnav=1".format(uid)
    #print(Referer)
    url='https://weibo.com/aj/mblog/fsearch'
    headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate,br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": cookies,
                "Host": "weibo.com",
                "Referer": Referer,
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
    param={
                "ajwvr": "6",
                "pre_page": "1",
                "page": "1",
                #"end_id": "1533473968009985",
                #"min_id": "4269615561508984",
                "leftnav": "1",
                "pagebar": "1",
                #"unread_max_id": "1533473968009970",
                #"unread_since_id": "1533473968009970",
                #"__rnd": "1533473999791"
            }
    r=requests.get(url,headers=headers,params=param,proxies=proxy)
    #print(r.status_code)
    ##print(demjson.decode(r.content)['data'])
    html=etree.HTML(demjson.decode(r.content)['data'])

    midList=html.xpath('/html/body/div/div[@action-type="feed_list_item"]/@mid')
    #print(midList)

    #mids=random.sample(midList,random.randint(1,4)-1)
    #print(mids)
    for each in midList:
        if random.randint(0,2) ==0:
            #time.sleep(random.randint(0,5))
            #print('进入点赞模块')
            addFab(cookies,each,proxy,su,'个人主页点赞',Referer)
        else:
            pass

proxy={"http": "http://111.230.129.13:11233"}
#addDlog(cookies,'nihao',proxy)
#getHost(cookies,proxy)
#getMblog('438793957@qq.com',cookies,proxy,)
#aaa=getUid(cookies,proxy)
