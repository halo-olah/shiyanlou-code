#coding=utf-8

import re

# re.match(正则表达式，要处理的字符串)  匹配字符串
# .：匹配除\n之外的任意字符，想要匹配\n，将re.S传入re.match()的参数里面
# []：匹配[]中的字符
# \d：匹配数字
# \D：匹配非数字
# \w：匹配英文、数字、_、中文 -----慎用
# \W：匹配非单词字符（特殊符号）
# \s：匹配空格和tab键等空白字符
# \S：匹配非空白字符
# {}:{n}表示{}前面的类型连续出现出现多少次，{n,m}表示{}前面的类型出现n-m次
# ?：？前面的数字只能出现0次或者1次
# *：*前面的字符可以出现任意次
# +：+前面的数字出现至少1次
# ^：匹配开头字符，放在最前面
# $：匹配结尾字符，放在最后面


hellos = ["hello,world","Hello,World","Hello,nihao,shijie,World"]
for hi in hellos:
    ret = re.match(r"[hH]ello\D",hi)
    if ret:
        # print(ret.group())
        continue


names = ["name1","_name","2_name","__name__"]
for name in names:
    ret = re.match(r"^[a-zA-Z_]+[\w]*$",name)
    if ret:
        # print(f"{ret.group()}:符合要求")
        continue
    else:
        # print(f"{name}:变量名不合法")
        continue


# 匹配163邮箱格式
mails = ["adahj@163.com","dadaf@163.comcom","1@163.com","dada@163.com@163.com"]
for mail in mails:
    ret = re.match(r"^[a-zA-Z1-9_]{4,20}@163\.com$",mail)
    if ret:
        # print(f"{ret.group()} 是163邮箱")
        continue
    else:
        # print(f"{mail}不是163邮箱")
        continue


# 分组功能()，类型于格式化，()数量与group()里面的数值匹配,\num表示第num个分组的值
# 给分组起别名，在分组里面使用 (?P<别名>) 给起别名，调用时，用(?P=别名) 来调用


# 正则表达式确认邮箱格式，并返回邮箱名称、类型、后缀
email = "ajdhajkh@163.com"
ret = re.match(r"^([a-zA-Z1-9_]{4,20})@(163|126|360)\.(com|cn)",email)
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))


# 用正则表达式确认标签是成对出现的
html_str1 = "<h1>dhaj121</h1>"
html_str2 = "<body><h1>ddekh2</h1></body>"
ret1 = re.match(r"^<(\w+)>.*</\1>$",html_str1)
ret2 = re.match(r"^<(\w+)><(\w+)>.*</\2></\1>$",html_str2)                              # \num调用法
ret3 = re.match(r"^<(?P<p1>\w+)><(?P<p2>\w+)>.*</(?P=p2)></(?P=p1)>$",html_str2)        # 别名调用法
# print(ret1.group())
# print(ret2.group())   
# print(ret3.group())


