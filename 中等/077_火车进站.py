"""
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
要求输出所有火车出站的方案，以字典序排序输出。
"""
N = int(input())
a = list(map(int, input().split()))
res = []
def dfs(order, inum, onum):
    if len(order) == N*2:
        stack = []
        tmp = []
        tmpa = a.copy()
        for o in order:
            if o == 'i':
                stack.append(tmpa.pop(0))
            else:
                tmp.append(str(stack.pop()))
        res.append(" ".join(tmp))
        return 
    if inum<N: 
        dfs(order+['i'], inum+1, onum)
    if onum<N and onum<inum: 
        dfs(order+['o'], inum, onum+1)
dfs(['i'], 1, 0)
res.sort()
for r in res:
    print(r)
