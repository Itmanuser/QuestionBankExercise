"""
IP地址是由4个0-255之间的整数构成的，用"."符号相连。
二进制的IP地址格式有32位，例如：10000011，01101011，00000011，00011000;每八位用十进制表示就是131.107.3.24
子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
"""
while True:
    try:
        x=input().split(".")
        y=input().split(".")
        z=input().split(".")
        m=[]
        n=[]
        for i in range(len(x)):
            x[i]=int(x[i])
            y[i] = int(y[i])
            z[i] = int(z[i])
        if x[0]!=255 or x[3]!=0 or max(x+y+z)>255 or min(x+y+z)<0:
            print("1")
        else:
            for i in range(len(x)):
                x[i]=bin(x[i]).replace("0b","")
                y[i] = bin(y[i]).replace("0b","")
                z[i] = bin(z[i]).replace("0b","")
                m.append(int(x[i],2)&int(y[i],2))
                n.append(int(x[i],2)&int(z[i],2))
            if m==n:
                print("0")
            else:
                print("2")
    except:
        break
