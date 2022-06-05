"""
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
输出一个正整数，为张强可以获得的最大的满意度。
"""
n, m = map(int,input().split())
primary , annex = {},{}
# 主键 附件
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:
        primary[i] = [x, y]
    else:
        if z in annex:
            annex[z].append([x, y])
        else:
            annex[z] = [[x,y]]
            
# 将主键和附件转换成dic 哈希化
m = len(primary)#主件个数转化为物品个数

dp = [[0]*(n+1) for _ in range(m+1)]
w, v= [[]], [[]]
for key in primary:
    w_temp, v_temp = [], []
    w_temp.append(primary[key][0])#1、主件
    v_temp.append(primary[key][0]*primary[key][1])
    if key in annex:#存在主件
        w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
        v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#存在两主件
            w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
            v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
            w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#400 、主件+附件1+附件2
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
for i in range(1,m+1):
    for j in range(10,n+1,10):#物品的价格是10的整数倍
        max_i = dp[i-1][j]
        for k in range(len(w[i])):
            if j-w[i][k]>=0:
                max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
        dp[i][j] = max_i
print(dp[m][n])


# while True:
#     try:
#         N, m = map(int,input().split())
#         res_dict = {}
#         for i in range(m):
#             v, p, q = map(int, input().split())
#             # 物品价格小于预算
#             if v <= N:
#                 # 物品属于主件
#                 if q == 0:
#                     if 0 in res_dict.keys():
#                         res_dict[0].append([v//10,v*p])
#                     else:
#                         res_dict[0] = [[v//10,v*p]]
#                 else:
#                     if q in res_dict.keys():
#                         res_dict[q].append([v//10,v*p])
#                     else:
#                         res_dict[q] = [[v//10,v*p]]
                        
#         print(res_dict)
#     except Exception as e:
#         print(e)
#         break