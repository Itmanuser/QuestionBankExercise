"""
按照指定规则对输入的字符串进行处理。
详细描述：
第一步：将输入的两个字符串str1和str2进行前后合并。
第二步：对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序
第三步：对排序后的字符串中的'0'~'9'、'A'~'F'和'a'~'f'字符，需要进行转换操作。
转换规则如下：
对以上需要进行转换的字符所代表的十六进制用二进制表示并倒序，然后再转换成对应的十六进制大写字符
如字符 '4'，其二进制为 0100 ，则翻转后为 0010 ，也就是 2 。转换后的字符为 '2'。
如字符 ‘7’，其二进制为 0111 ，则翻转后为 1110 ，对应的十进制是14，转换为十六进制的大写字母为 'E'。
如字符 'C'，代表的十进制是 12 ，其二进制为 1100 ，则翻转后为 0011，也就是3。转换后的字符是 '3'。
根据这个转换规则，由第二步生成的字符串 “abcedf” 转换后会生成字符串 "5D37BF"。
"""
def handle_paixu(n):
    jishu = []
    oushu = []
    for i in range(1,len(n)+1):
        if i % 2 == 0:
            oushu.append(n[i-1])
        else:
            jishu.append(n[i-1])
    jishu = sorted(jishu)
    oushu = sorted(oushu, reverse=False)
    new_n = ''
    for i in range(1, len(n)+1):
        if i % 2 != 0:
            new_n +=  jishu[(i-1)//2]
        else:
            new_n += oushu[(i-1) // 2]
    return new_n
            
def zhuai_n(n):
    res = []
    for i in n:
        if '0' <= i <= '9' or 'a' <= i <= 'f' or 'A' <= i <= 'F':
            b = bin(int(i, 16))[2:]
            b = '0' * (4 - len(b)) + str(b)
            h = hex(int(b[::-1], 2))[2:]
            if str(h).islower():
                h = h.upper()
            res.append(h)
        else:
            res.append(i)
    print(''.join(str(i) for i in res))
        
    
n = input().replace(' ', '')
new_n = handle_paixu(n)
zhuai_n(new_n)