"""
一组输入整数序列I和一组规则整数序列R，I和R序列的第一个整数为序列的个数（个数不包含第一个整数）；
整数范围为0~(2^31)-1，序列个数不限
"""

while True:
    try:
        I = input().split() 
        R = input().split()
        I_len = int(I[0]) #I[0]为I的数的个数
        I.remove(I[0]) #从I中去掉I[0]
        R_len = int(R[0]) #R的操作同上
        R.remove(R[0])
        R = list(set(R)) #R去重
        for i in range(len(R)): #先将R转为int类再排序，不能按str排序
            R[i] = int(R[i])
        R.sort() #R排序
        for i in range(len(R)):
            R[i] = str(R[i]) #再转为str（为了方便后续的操作）
        #print(R)
        s = []

        for i in range(len(R)):#判断R中的每个数
            num = 0
            for j in range(len(I)): #先判断I中有多少个包含R【i】的数
                if(R[i] in I[j]):
                    num += 1
            if(num == 0):#如果没有则直接跳过
                continue
            s.append(R[i]) #把R[i]放入S
            s.append(str(num))#把计数放入S
            for j in range(len(I)):
                if(R[i] in I[j]):
                    s.append(str(j))#把I中每个包含R[i]的位置和数分别放入S
                    s.append(I[j])
        s.insert(0,str(len(s))) #将S中有多少个数放在S的最开始
        print(' '.join(s)) #再将其中的数据合并成字符串
    except:
        break