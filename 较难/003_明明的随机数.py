"""
N个1到500之间的随机整数。
删去其中重复数字，然后再把这些数从小到大排序输出
"""
import sys

nums = []
while True:
    try:
        n = int(input())
        nums.append(n)
    except:
        break
        
n_nums = nums[1:]
n_nums = list(set(n_nums))
n_nums.sort(reverse=False)
m = map(lambda x: str(x), n_nums)
print("\n".join(m))