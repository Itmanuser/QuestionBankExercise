"""
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
"""
while True:
    try:
        s=input()
        l=[0,0,0]
        for i in s:
            l[0]+=int(i.isalpha())
            l[1]+=int(i==' ')
            l[2]+=int(i.isnumeric())
        print(l[0])
        print(l[1])
        print(l[2])
        print(len(s)-l[0]-l[1]-l[2])
    except:
        break