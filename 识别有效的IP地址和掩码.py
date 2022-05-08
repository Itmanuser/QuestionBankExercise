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