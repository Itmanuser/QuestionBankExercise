"""
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出
"""
while True:
    try:
        n = int(input())
        res = []
        for i in range(n):
            res.append(str(n*(n-1)+1+(i*2)))
        print("+".join(res))
    except:
        break 