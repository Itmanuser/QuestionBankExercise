"""
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度;
所谓回文串，指左右对称的字符串。
"""
while True:
    try:
        n = input()
        max_num = 0
        for i in range(len(n)):
            for j in range(i+1, len(n)+1):
                if n[i:j] == n[i:j][::-1] and j-i > max_num:
                    max_num = j-i 
        print(max_num)                   
    except:
        break 