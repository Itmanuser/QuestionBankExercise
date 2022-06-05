"""具体规则如下:
1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
2.每三位数后记得带上计数单位 分别是thousand, million, billion.
3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and
"""
num1 = ['zero','one','two','three','four','five','six',
       'seven','eight','nine','ten','eleven','twelve',
       'thirteen','fourteen','fifteen','sixteen',
       'seventeen','eighteen','nineteen']
num2 = [0,0,'twenty','thirty','forty','fifty','sixty',
       'seventy','eighty','ninety']

# 100以内转英文
def n2w(n):
    if n > 0:
        if n < 20:
            word.append(num1[n])
        else:
            word.append(num2[n//10])
            if n%10 != 0:
                word.append(num1[n%10])

# 1000以内转英文
def hun(n):
    if n >= 100:
        word.append(num1[n//100])
        word.append('hundred')
        if n % 100 != 0:
            word.append('and')
    n2w(n%100)

while True:
    try:
        n = int(input())
    except:
        break
    else:
        word = []
        a = n % 1000  # 个十百位
        b = (n//1000) % 1000  # 个十百千
        c = (n//1000000) % 1000  #个十百m
        d = n // 1000000000    # 个十百b
        if d > 0:
            hun(d)
            word.append('billion')
        if c > 0 :
            hun(c)
            word.append('million')
        if b > 0:
            hun(b)
            word.append('thousand')
        if a > 0 :
            hun(a)
        print(' '.join(word))
