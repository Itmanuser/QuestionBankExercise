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