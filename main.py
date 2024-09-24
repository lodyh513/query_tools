import thread
import argparse

def main():
    try:
        logo = '''
                                    _              _
      __ _ _   _  ___ _ __ _   _   | |_ ___   ___ | |___
     / _` | | | |/ _ \\ '__| | | |  | __/ _ \\ / _ \\| / __|   
    | (_| | |_| |  __/ |  | |_| |  | || (_) | (_) | \\__ \\
     \\__, |\\__,_|\\___|_|   \\__, |___\\__\\___/ \\___/|_|___/   
        |_|                |___/_____|
        '''
        print("\033[92m" + logo + "\033[0m")
    except SyntaxWarning as e:
        pass
    print('\n【++】Thorns纯享版v1.0   数据来源：爱站网\n【++】项目地址：https://github.com/lodyh513/query_tools\n【++】目前工具支持网站权重查询，备案信息查询等\n')
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url", required=False,help=f'指定目标URL')
        parser.add_argument("-f", "--files", required=False,help=f'指定目标txt文件，一行一个')
        #parser.add_argument("-b",default=0,required=False,help=f'指定百度权重不小于某值,范围0~10，默认为0')
        args = parser.parse_args()
        url = args.url
        files = args.files
        #parser.parse_args()
        thread.thread(url,files)
    except:
        pass

if __name__ == '__main__':
    main()