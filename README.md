# query_tools - 支持批量网站权重及备案查询
  在挖SRC时，批量提交报告时需要确定目标的权重、备案等，本工具可实现批量查询网站权重、企业备案信息，提高挖掘效率。

# 使用说明
安装依赖：
''' python
pip install -r requirements.txt

用法：
''' python
usage: main.py [-h] [-u URL] [-f FILES]
options:
  -h, --help            show this help message and exit
  -u URL, --url URL     指定目标URL
  -f FILES, --files FILES
                        指定目标txt文件，一行一个
