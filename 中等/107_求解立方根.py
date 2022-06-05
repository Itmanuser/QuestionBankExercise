"""
计算一个浮点数的立方根，不使用库函数。
保留一位小数。
"""

n = float(input())
if n == 0:
    print(0.0)
elif n > 0:
    sig = 1
else:
    sig = -1

n = abs(n)
if n >= 1:
    start = 1
    end = n 
else:
    start = n
    end = 1
mid = (start + end) / 2
while abs(mid ** 3 - n) > 0.001:
    if mid ** 3 > n:
        end = mid
    else:
        start = mid
    mid = (start + end) / 2
print(round(sig * mid, 1))
