import requests
from lxml import etree

def seo_query(url):
    urls = f"https://www.aizhan.com/cha/{url}"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,vi;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.aizhan.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
    }
    response = requests.get(url=urls, headers=headers)
    ahtml = etree.HTML(response.text)
    title = ahtml.xpath('//div[@id="webpage_title"]//text()')
    print(f"\n-> 域名：{url.replace('\n','')}\t\tTitle信息: {''.join(title)}")
    br = ahtml.xpath('//a[@id="baidurank_br"]//img//@alt')
    mbr = ahtml.xpath('//a[@id="baidurank_mbr"]//img//@alt')
    pr = ahtml.xpath('//a[@id="360_pr"]//img//@alt')
    sm_pr = ahtml.xpath('//a[@id="sm_pr"]//img//@alt')
    sogou_pr = ahtml.xpath('//a[@id="sogou_pr"]//img//@alt')
    google_pr = ahtml.xpath('//a[@id="google_pr"]//img//@alt')
    print(f"[+] 综合权重 \n   百度权重:{''.join(br)}\t移动权重:{''.join(mbr)}\t360权重:{''.join(pr)}\t神马权重:{''.join(sm_pr)}\t搜狗权重:{''.join(sogou_pr)}\t谷歌PR:{''.join(google_pr)}")
