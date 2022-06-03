"""
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
"""
n = input()
n_new = sorted(set(n))
nn = sorted(n_new,key=lambda x : n.count(x),reverse=True)
print("".join(nn))