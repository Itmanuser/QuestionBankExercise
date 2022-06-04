"""
将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。
"""
while True:
    try:
        n = int(input())
        n_list = list(map(int,input().split()))
        m = int(input())
        m_list = list(map(int,input().split()))
        sum_list = list(set(n_list+m_list))
        res = sorted(sum_list)
        print(''.join(map(str, res)))
    except:
        break