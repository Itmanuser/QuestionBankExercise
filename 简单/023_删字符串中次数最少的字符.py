"""
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
"""

def handle_n(n):
    res_dict = {}
    for i in n:
        s = n.count(i)
        res_dict[i] = s
    MIn = min(res_dict.values())4
    for i in n:
        if res_dict[i] == MIn:
            n = n.replace(i, "")
    print(n)

if __name__ == "__main__":
    while True:
        try:
            n = input()
            handle_n(n)
        except:
            break