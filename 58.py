import base64
import requests,os,time
from lxml import etree
def down(url):
    detailresult=etree.HTML(requests.get(url,headers=headers).text)
    print(detailresult.text.split("base64,")[1].split("'")[0].strip())
    money=detailresult.xpath('//div[@class="house-basic-right fr"]//div[@class="house-pay-way f16"]//b[@class="f36 strongbox"]/text()')
    base64_string = detailresult.text.split("base64,")[1].split("'")[0].strip()
    # 将 base64 编码的字体字符串解码成二进制编码
    bin_data = base64.decodebytes(base64_string.encode())
    # 保存为字体文件
    with open('58font.woff', 'wb') as f:
        f.write(bin_data)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
url='https://hz.58.com/chuzu/?PGTID=0d100000-0004-fa1d-33d1-dec32394de7d&ClickID=2'
result=etree.HTML(requests.get(url,headers=headers).text)
fangzi=result.xpath('//div[@class="list-wrap"]//div[@class="list-box"]/ul/li')[0]
print(fangzi.xpath('./div[@class="des"]/h2/a/@href')[0])
# for i in fangzi:
down(fangzi.xpath('./div[@class="des"]/h2/a/@href')[0])

