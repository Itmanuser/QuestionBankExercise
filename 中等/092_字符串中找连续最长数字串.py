"""
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输出（按原字符串的相对位置）
"""
import re 
while True:
    try:
        n = input()
        result = re.findall(r'\d+', n)
        max_nums = max(int(len(i)) for i in result)
        for res in result:
            if len(res) == max_nums:
                print(res,end='')
        print(","+str(max_nums))
    except:
        break 