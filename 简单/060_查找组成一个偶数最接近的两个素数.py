"""
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，
本题目要求输出组成指定偶数的两个素数差值最小的素数对。
"""
while True:
    try:
        n = int(input())
        res_list = []
        for i in range(int(n/2), 1,-1):
            for x in range(2,i):
                if i % x == 0 or (n-i) % x == 0:
                    break
            else:
                res_list.append(i)
        print(res_list[0])
        print(n-res_list[0])
    except:
        break
