# coding=utf-8
import requests
from lxml import etree
url='https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
result=requests.get(url,headers=headers)
lis=etree.HTML(result.text)
ul=lis.xpath('//li[@class="rank-item"]')
t=etree.tostring(lis,encoding='utf-8',)
save=[]
i=0
for lis in ul:
    title=lis.xpath('//a[@class="title"]//text()')[i]
    autor=lis.xpath('//div[@class="detail"]/a/span//text()')[i]
    watch=lis.xpath('//div[@class="detail"]//i[@class="b-icon play"]/..//text()')[i]
    bomb=lis.xpath('//div[@class="detail"]//i[@class="b-icon view"]/..//text()')[i]
    num=lis.xpath('//div[@class="num"]//text()')[i]
    lianjie=lis.xpath('//div[@class="img"]/a/@href')[i]
    sav={
        "b站全站排行榜第"+num+"名视频名称为":title,
        "up主为":autor,
        "视频播放量为":watch,
        "弹幕数为":bomb+'条',
        "视频链接为":lianjie,
    }
    save.append(sav)
    if i<100:
        i+=1
for i in save:
    print(i)