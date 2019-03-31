import time
import requests
import demjson
from lxml import etree
import random

#点赞功能
def addFab(mid):
    print('点赞：')
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
        "Cookie": "login_sid_t=be31bfba07dba1fac21c4da7af376e26;cross_origin_proto=SSL;_s_tentry=passport.weibo.com;Apache=7229076204960.079.1533363939224;SINAGLOBAL=7229076204960.079.1533363939224;ULV=1533363939231:1:1:1:7229076204960.079.1533363939224:;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbVQ12Y_zFkFbouHoG8yjr5JpX5K2hUgL.FoqfeoBES0zf1h22dJLoI0qLxKMLBKML12zLxKML1K.LB.BLxKML1K.LB.BLxKML1K.LB.BLxK-LBo5L1hqLxK-L1hqL1-zt;ALF=1564899957;SSOLoginState=1533363958;SCF=AjG1GXVMcFauKX88Is1cZsAZrv1-BoJRYrAVtzo9YkhLT-nqD_lxRqIfGOwpYf5l5wrgSvXRYIANGSG6kqsdO-I.;SUB=_2A252YTamDeRhGeBL6VYT9yzJwz2IHXVVFy9urDV8PUNbmtBeLWn6kW9NRyDzUF8wcGBYExScB__1LLI0CtnRMFjL;SUHB=0LcSGzVr7ZSmTu;un=13197667681;wvr=6;YF-Page-G0=35f114bf8cf2597e9ccbae650418772f;wb_view_log_6524272581=1536*8641.25",
        "Host": "weibo.com",
        "Origin": "https://weibo.com",
        "Referer": "https://weibo.com/3914359348/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    postData = {
    #"location": "page_100505_home",
    "version": "mini",
    "qid": "heart",
    "mid": mid,
    "loc": "profile"
}
    r=cok.post(url,params=param,headers=header,data=postData)
    if demjson.decode(r.content)['code'] == '100000':
        print('状态码为【{}】,微博【{}】点赞成功！'.format(demjson.decode(r.content)['code'],mid))
    else:
        print('未知错误{}'.format(demjson.decode(r.content)['code']))

def reBlog(mid,referer):
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
                "Cookie": "SINAGLOBAL=8226162695216.379.1533129695377;un=13197667681;wvr=6;wb_timefeed_6524272581=1;YF-Page-G0=5c7144e56a57a456abed1d1511ad79e8;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbVQ12Y_zFkFbouHoG8yjr5JpX5KMhUgL.FoqfeoBES0zf1h22dJLoI0qLxKMLBKML12zLxKML1K.LB.BLxKML1K.LB.BLxKML1K.LB.BLxK-LBo5L1hqLxK-L1hqL1-zt;ALF=1564903802;SSOLoginState=1533367803;SCF=AjG1GXVMcFauKX88Is1cZsAZrv1-BoJRYrAVtzo9YkhLYAiMmIHYSjYRUITVWQRjcPjQqvLazmt0gvGUa_RUkFY.;SUB=_2A252YSWrDeRhGeBL6VYT9yzJwz2IHXVVFxBjrDV8PUNbmtBeLUutkW9NRyDzUITaaq5CxE1Kx5MEavGIahV4mq-a;SUHB=0ebt1nsfFIvl4_;_s_tentry=login.sina.com.cn;UOR=,,login.sina.com.cn;Apache=6209471718915.185.1533367802576;ULV=1533367802583:2:2:2:6209471718915.185.1533367802576:1533129695382;YF-V5-G0=694581d81c495bd4b6d62b3ba4f9f1c8;wb_view_log_6524272581=1536*8641.125;WBStorage=e8781eb7dee3fd7f|undefined",
                "Host": "weibo.com",
                "Origin": "https://weibo.com",
                "Referer": referer,
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
    r=requests.post(url,headers=head,params=parm,data=postData)
    print(r.text)
    print('转发【{}】成功'.format(mid))



if __name__ == '__main__':
    rnd=str(time.time()).replace('.','')[:13]
    url='https://d.weibo.com/p/aj/discover/loading'
    head={
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "login_sid_t=be31bfba07dba1fac21c4da7af376e26;cross_origin_proto=SSL;_s_tentry=passport.weibo.com;Apache=7229076204960.079.1533363939224;SINAGLOBAL=7229076204960.079.1533363939224;ULV=1533363939231:1:1:1:7229076204960.079.1533363939224:;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbVQ12Y_zFkFbouHoG8yjr5JpX5K2hUgL.FoqfeoBES0zf1h22dJLoI0qLxKMLBKML12zLxKML1K.LB.BLxKML1K.LB.BLxKML1K.LB.BLxK-LBo5L1hqLxK-L1hqL1-zt;ALF=1564899957;SSOLoginState=1533363958;SCF=AjG1GXVMcFauKX88Is1cZsAZrv1-BoJRYrAVtzo9YkhLT-nqD_lxRqIfGOwpYf5l5wrgSvXRYIANGSG6kqsdO-I.;SUB=_2A252YTamDeRhGeBL6VYT9yzJwz2IHXVVFy9urDV8PUNbmtBeLWn6kW9NRyDzUF8wcGBYExScB__1LLI0CtnRMFjL;SUHB=0LcSGzVr7ZSmTu;un=13197667681;wvr=6;YF-Page-G0=35f114bf8cf2597e9ccbae650418772f;wb_view_log_6524272581=1536*8641.25",
        "Host": "d.weibo.com",
        "Referer": "https://d.weibo.com/623751_1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    parm={
        "ajwvr": "1",
        "id": "623751_1",
        # "uid": "6524272581",
        "page": "1",
        # "__rnd": rnd
    }
    r=requests.get(url,headers=head,params=parm)
    #req=demjson.decode(r.text)['data']['html']
    html=etree.HTML(demjson.decode(r.text)['data']['html'])
    content=html.xpath('//*[@class="pt_li pt_li_2 S_bg2"]/@href')
    contentLink=[]
    for each in content:
        if each[:6] != 'https:':
            contentLink.append('https:'+each)
        else:
            contentLink.append(each)

    while True:
        head2={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "SINAGLOBAL=8226162695216.379.1533129695377;un=13197667681;wvr=6;wb_timefeed_6524272581=1;YF-Page-G0=5c7144e56a57a456abed1d1511ad79e8;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbVQ12Y_zFkFbouHoG8yjr5JpX5KMhUgL.FoqfeoBES0zf1h22dJLoI0qLxKMLBKML12zLxKML1K.LB.BLxKML1K.LB.BLxKML1K.LB.BLxK-LBo5L1hqLxK-L1hqL1-zt;ALF=1564903802;SSOLoginState=1533367803;SCF=AjG1GXVMcFauKX88Is1cZsAZrv1-BoJRYrAVtzo9YkhLYAiMmIHYSjYRUITVWQRjcPjQqvLazmt0gvGUa_RUkFY.;SUB=_2A252YSWrDeRhGeBL6VYT9yzJwz2IHXVVFxBjrDV8PUNbmtBeLUutkW9NRyDzUITaaq5CxE1Kx5MEavGIahV4mq-a;SUHB=0ebt1nsfFIvl4_;_s_tentry=login.sina.com.cn;UOR=,,login.sina.com.cn;Apache=6209471718915.185.1533367802576;ULV=1533367802583:2:2:2:6209471718915.185.1533367802576:1533129695382;YF-V5-G0=694581d81c495bd4b6d62b3ba4f9f1c8;wb_view_log_6524272581=1536*8641.125;WBStorage=e8781eb7dee3fd7f|undefined",
            "Host": "weibo.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
        }
        Pageurl=contentLink[random.randint(0,len(contentLink)-1)]
        print(Pageurl)
        r=requests.get(Pageurl,headers=head2)
        print('状态码',r.status_code)
        html=etree.HTML(r.text)
        mid=html.xpath('//*[@id="plc_main"]/div/div/div/div[5]/div/div/@mid')[0]
        #print(mid)
        addFab(mid)
        time.sleep(random.randint(10,20))
        reBlog(mid,Pageurl)
        break
