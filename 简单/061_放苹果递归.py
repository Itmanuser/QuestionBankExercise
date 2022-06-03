# 把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法
def fun(m,n):
    if m < 0 or n < 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return f(m,n-1) + f(m-n,n)
    
if __name__ == "__main__":
    while True:
        try:
            m, n = map(int,input().split())
            print(fun(m,n))
        except:
            break