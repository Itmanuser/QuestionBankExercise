"""
现在有一种密码变换算法。
九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
数字和其它的符号都不做变换。
"""
while True:
    try:
        res = []
        n = input()
        for i in n:
            if i in "abc":
                i = "2"
            elif i in "def":
                i = "3"
            elif i in "ghi":
                i = "4"
            elif i in "jkl":
                i = "5"
            elif i in "mno":
                i = "6"
            elif i in "pqrs":
                i = "7"
            elif i in "tuv":
                i = "8"
            elif i in "wxyz":
                i = "9"
            elif i.isupper() and i =="Z":
                i = "a"
            elif i.isupper() and i != "Z":
                i = chr(ord(i)+33)
            res.append(i)
        print("".join(res))
            
    except:
        break 