import requests
import json
import os
num=1
def img(num,name):
    param={
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'queryWord': str(name),
    'cl': '2',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid':'',
    'st':'',
    'z':'',
    'ic':'',
    'hd':'',
    'latest':'',
    'copyright':'',
    'word': str(name),
    's':'',
    'se':'',
    'tab':'',
    'width':'',
    'height':'',
    'face':'',
    'istype':'',
    'qc':'',
    'nc':'',
    'fr':'',
    'expermode':'',
    'force':'',
    'pn':str(num),
    'rn': '30',
    '1587183189928':''
    }
    result=json.loads(requests.get('https://image.baidu.com/search/acjson?',params=param).text).get('data')
    list=[]
    for i in result:
        list.append(i['thumbURL'])
    print('下载完毕')
    return list
def save(list,name):
    global num
    if not os.path.exists(('D:\\{}').format(name)):
        os.makedirs(('D:\\{}').format(name))
    for i in list:
        print(i)
        path = 'D:\\{}\\{}.jpg'.format(name,num)
        num += 1
        img=requests.get(i,timeout=2).content
        with open(path,'wb') as save:
            save.write(img)
if __name__ == '__main__':
    print('请输入名称以及要下载几页')
    name=input()
    num=input()
    if num=='1':
        num='2'
    for i in range(2,int(num)+1):
        list=img(30*i,name)
        print(list)
        save(list,name)
    print('执行结束')
