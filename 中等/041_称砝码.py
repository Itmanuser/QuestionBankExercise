"""
现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
"""
while True:
    try:
        fm_type = int(input())
        m = list(map(int,input().split()))
        x = list(map(int,input().split()))
        # 获取所有的砝码
        res = []
        for i in range(fm_type):
            for j in range(x[i]):
                res.append(m[i])
        # 根据所有砝码进行计算所有可能重量
        weight = {0}
        for i in res:
            for j in list(weight):
                weight.add(i+j)
        print(len(weight))       
    except:
        break