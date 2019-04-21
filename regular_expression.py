import re

match = re.search(r'^(?P<scheme>http)://(?P<netloc>\w+(\.\w+)+)/(?P<path>\w+)\?(?P<query>\w+=\w+(&\w+=\w+)*)$', 'http://www.google.com/query?w=123&t=456')
print(match.group(0))

# 模擬將 urllib.parse.urlparse 回傳的 ParseResult 資料取出
print(match.group('scheme'))
print(match.group('netloc'))
print(match.group('path'))
print(match.group('query'))
