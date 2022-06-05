"""
在命令行输入如下命令：
xcopy /s c:\\ d:\\e，
各个参数如下：
参数1：命令字xcopy
参数2：字符串/s
参数3：字符串c:\\
参数4: 字符串d:\\e
请编写一个参数解析程序，实现将命令行各个参数解析出来。
"""
import re
while True:
    try:
        n = input()
        if n.count('"') == 0:
            res = n.split()
            print(len(res))
            print("\n".join(res))
        else:
            s = re.findall(r'\".*?\"', n)
            for i in s:
                t = i.replace(r' ', '$')
                t = t.replace('"', '')
                n = n.replace(i, t)
            res = n.split()
            print(len(res))
            for r in res:
                print(r.replace('$', " "))
    except:
        break