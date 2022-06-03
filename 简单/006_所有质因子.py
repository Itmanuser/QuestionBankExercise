##输入一个正整数，按照从小到大的顺序输出它的所有质因子(如180的质因子为2 2 3 3 5 ）
import math 
while True:
    try:
        n = int(input())
        for i in range(2,int(math.sqrt(n)+1)):
            while n % i == 0:
                print(i, end=' ')
                n = n // i
        if n > 2:
            print(n)
    except:
        break
