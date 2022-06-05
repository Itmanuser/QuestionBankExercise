"""
对输入的字符串进行加解密，并输出。
加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
解密方法为加密的逆过程。
"""

input_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
output_str = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
while True:
    try:
        jiami = input()
        jiemi = input()
        jia_str = ''
        jie_str = ''
        for i in jiami:
            if i in input_str:
                jia_str += output_str[input_str.index(i)]
            else:
                jia_str += i
        print(jia_str)
        for j in jiemi:
            if j in output_str:
                jie_str += input_str[output_str.index(j)]
            else:
                jie_str += j
        print(jie_str)
    except:
        break