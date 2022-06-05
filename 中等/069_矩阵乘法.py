"""
输入描述：
第一行包含一个正整数x，代表第一个矩阵的行数
第二行包含一个正整数y，代表第一个矩阵的列数和第二个矩阵的行数
第三行包含一个正整数z，代表第二个矩阵的列数
之后x行，每行y个整数，代表第一个矩阵的值
之后y行，每行z个整数，代表第二个矩阵的值
"""
while True:
    try:
        n=int(input())
        m=int(input())
        s=int(input())
        firstArray=[]
        secondArray=[]
        for i in range(n):
            firstArray.append(list(map(int, input().split())))
        for j in range(m):
            secondArray.append(list(map(int, input().split())))
        res=[[0 for i in range(s)] for j in range(n)]
        for i in range(n):
            for j in range(s):
                for x in range(m):
                    res[i][j]+=firstArray[i][x]*secondArray[x][j]
        for e in res:
            print(' '.join(list(map(str, e))))
    except:
        break
