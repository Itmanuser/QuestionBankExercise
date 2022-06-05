"""
输出 1到n之间 的与 7 有关数字的个数。
一个数与7有关是指这个数是 7 的倍数，或者是包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）
"""
while True:
    try:
        n = int(input())
        res = []
        for i in range(1,n+1):
            if i % 7 == 0:
                res.append(i)
            elif "7" in str(i):
                res.append(i)
        print(len(res))
    except:
        break
            