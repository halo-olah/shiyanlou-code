#coding=utf-8

import re

# re.match(正则表达式，要处理的字符串)
ret1 = re.match(r"hello","hello,world")
ret2 = re.match(r"hello","Hello,world")
ret3 = re.match(r"[hH]ello","Hello,World")
print(ret1)
print(ret2)
print(ret3)