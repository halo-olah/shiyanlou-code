#coding=utf-8

import re

# re.search()用法:不会从头开始匹配，从匹配到匹配语句第一个字符开始匹配，在匹配语句前加 ^ 即可实现re.match()功能
ret = re.search(r"\d+","阅读次数为 9999 ")
# print(ret.group())


# re.findall():返回所有满足匹配条件的值,返回值直接输出，不用使用group方法
ret = re.findall(r"\d+","c = 100,python = 1000,java = 242,c++ = 643")
# print(ret)


# re.sub():替换，将第三个参数中满足匹配条件的内容替换为第二个参数，第二个参数可以为函数,仅python里有该用法
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret1 = re.sub(r"\d+","998","python = 999")
ret2 = re.sub(r"\d+",add,"python = 999")
# print(ret1,"\n",ret2)


# re.split():根据匹配进行切割字符串，并返回一个列表
