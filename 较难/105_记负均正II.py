"""
输入n个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
"""

def func(z_lists,f_lists):
    print(len(f_lists))
    res = sum(z_lists)
    if len(z_lists) > 0:
        avg = round(res/len(z_lists),1)
    else:
        avg = 0.0
    print(avg)
    
z_lists = []
f_lists = []
while True:
    try:
        n = int(input())
        if n > 0:
            z_lists.append(n)
        else:
            f_lists.append(n)            
    except:
        break        
func(z_lists,f_lists)