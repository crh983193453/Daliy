import requests
# from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/explore'
}
r=requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0',headers=headers)
# html=etree.HTML(r.text)
lis=r.json()
items=lis.get('subjects')
for item in items:
    li={}
    li['rate']=item.get('rate')
    li['name']=item.get('title')
    print(li)
