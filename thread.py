from concurrent.futures import ThreadPoolExecutor
import seo
import icp

def thread(url,files):
    if url:
        seo.seo_query(url=url)
        icp.icp_query(url=url)
    else:
        #去重处理
        list01 = []
        with open(files, "r", encoding="utf-8") as f:
            for i in f:
                if i in list01:
                    continue
                list01.append(i)
        # 创建最大线程数的线程池
        count = 0
        with ThreadPoolExecutor(10) as threadPool:
            for url in list01:
                try:
                    print('=================================================================='
                                  '==========================================')
                    threadPool.submit(seo.seo_query(url=url), url.replace("\n", ""))
                    threadPool.submit(icp.icp_query(url=url), url.replace("\n", ""))
                    count += 1
                except Exception as e:
                    print("[-] error: ", e)
                    continue
        print(f'\ntotle: [{count}]')