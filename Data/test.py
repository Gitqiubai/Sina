import demjson
import requests
from lxml import etree
import random
from Sina.doModle import addFab

if __name__ == '__main__':
    url='https://account.weibo.com/set/index'
    headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip,deflate,br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": 'ALC=ac%3D0%26bt%3D1533465988%26cv%3D5.0%26et%3D1565001988%26ic%3D1946859249%26login_time%3D1533465987%26scf%3D%26uid%3D5415830208%26vf%3D0%26vs%3D0%26vt%3D0%26es%3Dec276ab9e303595e5e0759cee0a6ca0f;LT=1533465988;tgc=TGT-NTQxNTgzMDIwOA==-1533465987-gz-22B4FB67C8C788119F014F4B3CF97AEB-1;ALF=1565001988;SCF=Aogw-2W3rUpiVy-b9T_NbfeDVQEpGA0XDCx_ZVirEfbBJxWlwHvCa0ZJmE_e9rA_NU7Z0ZfJHSZHqtrV1yi43pI.;SUB=_2A252YqXUDeRhGeNK6lcZ8y7OyzSIHXVVGZAcrDV_PUNbm9BeLXnMkW9NSVtpsjiVwZ8TkcNbe79CEkEp-lniU2ad;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWsOHfqchO1sJsjsSY0SDSQ5NHD95QfSh2f1he7eo5RWs4Dqcj.i--fi-zpi-zpi--fiKy2iK.Ni--ciKL8iKL2i--4iKL2iK.E;sso_info=v02m6alo5qztKWRk5SlkKOEpZCjhKWRk5SljoSQpY6TnKWRk5iljpSUpY6UkKWRk6SljpSQpY6TiKadlqWkj5OUtIyTlLiMs4CyjIOgwA==;',
                "Host": "account.weibo.com",
                "If-Modified-Since": "Sun,05Aug201814:59:08GMT",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
            }
    param={
                "topnav": "1",
                "wvr": "6"
            }
    r=requests.get(url,headers=headers,params=param)
    html=etree.HTML(r.content)
    data=html.xpath('/html/head/script[1]/text()')[0]
    #print(data)
    D=data.replace('$CONFIG = ','')
    print(demjson.decode(D)['uid'])
    #print(r.text)



