"""
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。
"""

while True:
    try:
        n = input()
        n = n.replace("{", "(")
        n = n.replace("}", ")")
        n = n.replace("[", "(")
        n = n.replace("]", ")")
        print(int(eval(n)))
    except:
        break