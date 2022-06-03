"""
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）
如果符合要求输出：OK，否则输出NG
"""
def check_n(n):
    if len(n) <= 8:
        return False
    s_num, b_num, int_num, o_num = 0, 0, 0, 0
    for i in n:
        if ord('a') <= ord(i) <= ord('z'):
            s_num = 1
        elif ord('A') <= ord(i) <= ord('Z'):
            b_num = 1
        elif ord('0') <= ord(i) <= ord('9'):
            int_num = 1
        else:
            o_num = 1
    sum = s_num + b_num + int_num + o_num
    if sum < 3:
        return False
    for i in range(len(n)-3):
        if len(n.split(n[i:i+3])) >= 3:
            return False
    return True

while True:
    try:
        n = input()
        flag = check_n(n)
        if flag:
            print("OK")
        else:
            print("NG")
    except:
        break
    