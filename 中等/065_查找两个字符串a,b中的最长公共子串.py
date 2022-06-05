"""
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开
"""
while True:
    try:
        short_str = input()
        long_str = input()
        if len(short_str) > len(long_str):
            short_str,long_str = long_str,short_str
        res = ""
        for i in range(0,len(short_str)):
            for j in range(i+1,len(short_str)):
                if short_str[i:j+1] in long_str and j+1-i > len(res):
                    res = "".join(short_str[i:j+1])
        print(res)     
    except:
        break