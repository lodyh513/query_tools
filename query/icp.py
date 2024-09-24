import requests
import re
from lxml import etree

def icp_query(url):
    urls = f"https://icp.aizhan.com/{url}/"
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://icp.aizhan.com/',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = requests.get(url=urls, headers=headers)
    ahtml = etree.HTML(response.text)

    name = ahtml.xpath('//div//tr[1]/td[2]/text()')
    name_1 = name[0]
    icp_name = re.split('\xa0\xa0',name_1)[0]

    nature = ahtml.xpath('//div//tr[2]/td[2]/text()')
    nature_1 = nature[0]
    icp_nature = re.split('\xa0\xa0', nature_1)[0]

    id = ahtml.xpath('//div//tr[3]/td[2]/span/text()')
    id_1 = id[0]
    icp_id = re.split('\xa0\xa0', id_1)[0]

    cap = ahtml.xpath('//div//tr[1]/td[2]/span[2]/text()')
    art = ahtml.xpath('//div//tr[2]/td[1]/span[2]/text()')
    web = ahtml.xpath('//div[4]/div[3]/div[2]/div[2]//tr[3]/td[2]/a/text()')
    addr = ahtml.xpath('//div[4]/div[3]/div[2]/div[2]//tr[3]/td[3]/span[2]/text()')
    print(f"[+] 备案信息")
    print(f"   主办单位名称:{icp_name}\t性质:{icp_nature}\t备案号:{icp_id}\t注册资本:{''.join(cap)}")
    print(f"   行业:{''.join(art)}\t官网:{''.join(web)}\t地址:{''.join(addr)}")

if __name__ == '__main__':
    pass