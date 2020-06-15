import queue
import threading
import time
headr = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
 'accept-encoding':'gzip, deflate, br',
 'accept-language':'zh-CN,zh;q=0.9',
 'cache-control':'max-age=0',
 'cookie':'PHPSESSID=i267p1vkesffuaqgk5ittavj4k; _ga=GA1.2.1980701794.1587954038; _gid=GA1.2.492162984.1587954038; nav_switch=booklist; CFWztgFirstShowTime_856_Cookie=2020-4-27%2010%3A20%3A49; CFWztgVisitTotal_856_Cookie=1; Hm_lvt_52ec474a2124c332da93cd0293a3980b=1587954049; Hm_lpvt_52ec474a2124c332da93cd0293a3980b=1587954049; _gat_gtag_UA_145781056_1=1',
 'referer':'https://www.hanmanjia.com/book/toptoon368',
 'sec-fetch-mode':'navigate',
 'sec-fetch-site':'same-origin',
 'sec-fetch-user':'?1',
 'upgrade-insecure-requests':'1',
 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'}
proxies = {'http': '60.13.42.23'}
num1=0
lock=threading.Lock()
class mythread(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.name=name
        self.q=q
    def run(self):
        job(self.name,self.q)
def job(threadname,num):
    global num1
    print(threadname + '开始工作')
    while not num.empty():
        lock.acquire()
        zhuan = num.get()
        print(threadname+'正在下载'+str(zhuan)+'图片')
        num1+=1
        print('这是第'+str(num1)+'张图片')
        lock.release()
        time.sleep(0.1)
if __name__ == '__main__':
    starttime=time.time()
    # q=queue.Queue()
    # url='https://www.hanmanjia.com/chapter/28977-166263'
    # html = etree.HTML(requests.get(url, headers=headr, proxies=proxies).text)
    # result = html.xpath('//div[@id="cp_img"]/img/@data-original')
    # for i in result:
    #     q.put(i)
    # for i in range(q.qsize()):
    #     print(q.get())
    q = queue.Queue()
    for i in range(20):
        q.put('https://www.hanmanjia.com/'+str(i))
    thread=mythread('一号',q)
    thread2=mythread('二号',q)
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    endtime=time.time()
    print('工作结束,总共花费'+str(endtime-starttime))

