"""
给定一些同学的信息（名字，成绩）序列，请你将他们的信息按照成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
"""
while True:
    try:
        n = int(input())
        if input() == "0":
            flag = True
        else:
            flag = False
        ls = []
        for i in range(n):
            name,score = input().split()
            ls.append((name,int(score)))
            ls.sort(key=lambda x:x[1], reverse = flag )
        for x in ls:
            print(*x)
    except:
        break