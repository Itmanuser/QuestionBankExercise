"""
输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，
并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），
不是5的倍数也不是3的倍数能放在任意一组，可以将数组分为空数组，能满足以上条件，输出true；不满足时输出false。
"""
while True:
    try:
        length = int(input())
        num_list = list(map(int, input().strip().split()))
        res = 0
        # 计算初始3,5倍数的差值
        for _ in range(length):
            i = num_list.pop(0)
            if i % 3 == 0:
                res += i
            elif i % 5 == 0:
                res -= i
            else:
                num_list.append(i)
        res = {res}
        # 结果计算，把之前结果，分别计算当前值的+和-2种情况，然后把结果再放回去，给下一次计算
        while num_list:
            i = num_list.pop(0)
            res_plus = [x + i for x in res]
            res_plus.extend([x - i * 2 for x in res_plus])
            res = set(res_plus)
        # 最后如果0值在结果中，表示可以算出，如果不在则不行
        if 0 in res:
            print('true')
        else:
            print('false')
    except:
        break