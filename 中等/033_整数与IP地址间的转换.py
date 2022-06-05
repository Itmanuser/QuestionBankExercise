"""
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
"""
while True:
    try:
        ip = input()
        num = input()
        ip_list = ip.split('.')
        ip2num = ""
        for i in ip_list:
            a = bin(int(i,10))[2:]
            a = a.rjust(8,'0')
            ip2num += a
        print(int(ip2num,2))
        
        num2ip = []
        num2 = bin(int(num,10))[2:]
        num2 = num2.rjust(32,'0')
        for i in range(4):
            b = num2[8*i:8*i+8]
            b = str(int(b,2))
            num2ip.append(b)
        print('.'.join(num2ip))
    except:
        break