"""
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址从1.0.0.0到126.255.255.255;B类地址从128.0.0.0到191.255.255.255;C类地址从192.0.0.0到223.255.255.255;D类地址从224.0.0.0到239.255.255.255；E类地址从240.0.0.0到255.255.255.255
私网IP范围是：
从10.0.0.0到10.255.255.255;从172.16.0.0到172.31.255.255.从192.168.0.0到192.168.255.255
子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）（注意二进制下全是1或者全是0均为非法子网掩码）
"""
# A、B、C、D、E、错误IP地址或错误掩码、私有IP
res = [0,0,0,0,0,0,0] 

def check_mask(mask):
    if not check_ip(mask):
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        return False
    mask_list = mask.split('.')
    if len(mask_list) != 4:
        return False
    mask_bit = []
    for i in mask_list:
        i = bin(int(i))
        i = i[2:] 
        mask_bit.append(i.zfill(8)) 
    whole_mask = ''.join(mask_bit)
    whole0_find = whole_mask.find("0")
    whole1_rfind = whole_mask.rfind("1")
    if whole1_rfind+1 == whole0_find:
        return True
    else:
        return False

def check_ip(ip):
    ip_bit = ip.split('.')
    if len(ip_bit) != 4 or '' in ip_bit:
        return False
    for i in ip_bit:
        if int(i)<0 or int(i) >255:
            return False
    return True

def check_private_ip(ip):
    ip_list = ip.split('.')
    if ip_list[0] == '10': return True
    elif ip_list[0] == '172' and 16<=int(ip_list[1])<=31: return True
    elif ip_list[0] == '192' and ip_list[1] == '168': return True
    return False

while True:
    try:
        s = input()
        ip = s.split('~')[0]
        mask = s.split('~')[1]
        if check_ip(ip):
            first = int(ip.split('.')[0])
            if first==127 or first==0:
                continue
            if check_mask(mask):
                if check_private_ip(ip):
                    res[6] += 1
                if 0<first<127:
                    res[0] += 1
                elif 127<first<=191:
                    res[1] += 1
                elif 192<=first<=223:
                    res[2] += 1
                elif 224<=first<=239:
                    res[3] += 1
                elif 240<=first<=255:
                    res[4] += 1
            else:
                res[5] += 1
        else:
            res[5] += 1
    except:
        break

for v in res:
    print(v,end=(' '))