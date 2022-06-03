"""
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28
"""
def handle(n):
    m = 0
    for i in range(1,n):
        if n % i == 0:
            m = m + i
    if m == n:
        return n
            
n = int(input())
res = []
for i in range(1,n):
    n = handle(i)
    if n:
        res.append(n)
print(len(res))
        