import requests
from lxml import etree
url='https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
result=requests.get(url,headers=headers)
neirong=etree.HTML(result.text)
list1=[]
for i in range(0,51):
    if i==50:
        break
    title=neirong.xpath('//tr[@class=""]/td[@class="td-02"]/a//text()')[i]
    num=neirong.xpath('//tr[@class=""]/td[@class="td-01 ranktop"]//text()')[i]
    redianliang=neirong .xpath('//tr[@class=""]/td[@class="td-02"]/span//text()')[i]
    save={
        "标题":title,
        "排名":num,
        "点击量":redianliang
    }
    list1.append(save)
for i in range(0,51):
    if i==50:
        break
    print(list1[i])
