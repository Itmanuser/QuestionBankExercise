"""
在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符
注意：匹配时不区分大小写。
"""
import re 

while True:
    try:
        pattern = input().lower()
        word = input().lower()
        pattern = pattern.replace('.','\.')
        pattern = pattern.replace('?','[0-9a-z]')
        pattern =  re.sub('(\*)+','[0-9a-z]*',pattern)
        res = re.fullmatch(pattern, word)
        if res:
            print("true")
        else:
            print("false")
    except:
        break