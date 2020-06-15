import time

import requests
import threading


class thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = ('thread' + name)

    def run(self):
        run(self.name)
failnum=0
def run(name):
    url='http://116.62.244.22:8000/cms/adddata/'
    head={
        'cookie':'id=id:1jfytu:INS_NwgsTSfdrL-BntrxiwL7sZQ; username=crh:1jfytu:V6LLYnuYvyFnx3-QQjfkBu9ly6I'
    }
    for i in range(200):
        data={
            'name':(str(name)+str(i)),
            'banji':'软件181',
            'reason':'事假',
            'data':'1.1',
            'detail':'1-8'
        }
        global failnum
        a=requests.post(url,data=data,headers=head)
        Lock=threading.Lock()
        if(a.status_code!=200):
            Lock.acquire()
            failnum+=1
            Lock.release()
        print(str(name)+'正在请求')
    # global num
    # lock = threading.Lock()
    # while num > 0:
    #     lock.acquire()
    #     print(str(name) + '正在搬第' + str(num) + '块砖')
    #     num -= 1
    #     lock.release()
    #     time.sleep(0.1)
if __name__ == '__main__':
    list = []
    for i in range(50):
        list.append(thread(str(i)))
    for i in list:
        i.start()
    for i in list:
        i.join()
    print(failnum)
