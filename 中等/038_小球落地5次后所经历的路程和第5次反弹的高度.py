"""
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
"""
while True:
    try:
        res = []
        n = int(input())
        for i in range(6):
            res.append(n*0.5**i)
        sums = res[0] + 2*res[1]+ 2*res[2]+2*res[3]+ 2*res[4] 
        print(sums) 
        print(res[-1])
    except:
        break 