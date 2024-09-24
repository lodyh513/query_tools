import thread
import argparse

def main():
    try:
        logo = f'''
                                    _              _
      __ _ _   _  ___ _ __ _   _   | |_ ___   ___ | |___
     / _` | | | |/ _ \ '__| | | |  | __/ _ \ / _ \| / __|   Thorns纯享版v1.0   数据来源：爱站网
    | (_| | |_| |  __/ |  | |_| |  | || (_) | (_) | \__ \\
     \__, |\__,_|\___|_|   \__, |___\__\___/ \___/|_|___/   https://
        |_|                |___/_____|
        '''
        print("\033[92m" + logo + "\033[0m")
    except SyntaxWarning as e:
        pass
    print('\n目前工具支持网站权重查询，备案信息查询等')
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url", required=False,help=f'指定目标URL')
        parser.add_argument("-f", "--files", required=False,help=f'指定目标txt文件，一行一个')
        parser.add_argument("-b",default=0,required=False,help=f'指定百度权重不小于某值,范围0~10，默认为0')
        args = parser.parse_args()
        url = args.url
        files = args.files
        parser.parse_args()
        thread.thread(url,files)
    except:
        pass

if __name__ == '__main__':
    # seo_query(url='nanshan.edu.cn')
    # icp_query(url='nanshan.edu.cn')
    main()
# for i in range(11):
#     print(f"'{i}',",end='')