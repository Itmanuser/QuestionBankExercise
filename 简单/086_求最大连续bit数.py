"""
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
数据范围：数据组数：1≤t≤5 ，1≤n≤500000 
"""
while True:
    try:
        n = int(input())
        m = bin(n)
        res = m.split("0b")[-1]
        result = res.split("0")
        result = sorted(result,reverse=True)
        print(len(result[0]))
    except:
        break 