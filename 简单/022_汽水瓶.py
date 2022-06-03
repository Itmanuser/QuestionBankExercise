"""
三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）;
小张手上有n个空汽水瓶，最多可以喝到多少瓶汽水
"""
def func(n):
    res = n // 3
    s = n // 3 + n % 3
    if s < 2:
        res += 0
    elif s == 2:
        res += 1
    else:
        res += func(s)
    return(res)
  
if __name__ == "__main__":
    while True:
        try:
            n  = int(input())
            if n == 0:
                break
            print(func(n))
        except:
            break