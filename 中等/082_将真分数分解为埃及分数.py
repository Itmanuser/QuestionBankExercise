"""
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，
请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
"""
while True:
    try:
        a,b = list(map(int,input().split('/')))
        flag = True
        t=[]
        while flag:
            p = int(b/a)
            r = int(b%a)
            if r==0 and a > 1:
                t.append('1'+'/'+ str(p))
                flag=False
            elif a==1:
                t.append('1'+'/'+ str(b))
                flag = False
            else:
                t.append('1'+'/'+ str(p+1))
                a = a-r
                b = b*(p+1)
        print("+".join(t))        
    except:
        break
