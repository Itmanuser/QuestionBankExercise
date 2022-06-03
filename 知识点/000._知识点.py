"""
其中简单不需要代码题目编号: 001、002、004、007、009、011、012、013、014、015、034、046、054、057、058、062、081、084、099、106；
共计：题
知识点包含题目编号： 005、008、010、073；
共计：题
"""
## 005：进制转换
int(nums, 16)
## 008：tmp字典排序：
tmp1 = sorted(tmp.items(),key=lambda x: int(x[0]))
## 010：字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )
0 <= ord(i) <= 127
## 取余数：%
## 073：输入的日期，计算是这一年的第几天
data = datetime.datetime(year,month,day)
days = data.strftime("%j").lstrip("0")
## 096:字符中所有出现的数字前后加上符号“*”
pre.sub('(\d+)', "*\g<1>*", n)
## 097:结果保留一位小数
round(sum(z_list) / len(z_list),1)
## 100：等差数列 2，5，8...求等差数列前n项和
res=n*2+ n*(n-1)*3/2
## X先变成小写，再往后移一位(ord("A"))
if i.isupper() and i != "Z":
    i = chr(ord(i)+33)
## 不能有长度大于2的包含公共元素的子串重复
for i in range(len(n)-3):
    if len(n.split(n[i:i+3])) >= 3:
        return False

