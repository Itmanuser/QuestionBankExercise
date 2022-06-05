"""
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。
他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？
"""
while True:
    try:
        num = int(input())
        lst = list(map(int,input().split()))
        l = len(lst) #序列长度
        if(l == 1):
            print(1)
        else:
            data = [1]*l #记录每个数字的前面的最长升序子序列
            for i in range(1,l): #从第二个数字开始
                for j in range(i): #从第一个数字开始到第i+1个
                    if(lst[i] > lst[j]):  #若找到的数字小于第i+1个数字
                        data[i] = max(data[i],data[j] + 1) #data记录的是当前数字之前的公共子序列长度
        print(max(data))
    except:
        break
