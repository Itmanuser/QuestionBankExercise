"""
给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个字符串，计算每个字符串最大可能的“漂亮度”。
"""
while True:
    try:
        n = int(input())
        for i in range(n):
            m = input()
            res_dict = {}
            sums = 0
            set_m = set(m)
            for st in set_m:
                res_dict[st] = m.count(st)
            res_list = sorted(res_dict.values(),reverse=True)
            for i in range(len(res_list)):
                sums = sums + (res_list[i] * (26-i))
            print(sums)
                
    except Exception as e:
        print(e)
        break 
