"""有一个m*n\m∗n 大小的数据表，你会依次进行以下5种操作：
1.输入m\m 和n\n ，初始化m*n\m∗n 大小的表格。
2.两个数交换坐标
3.输入x\x ，在第x\x 行上方添加一行。
4.输入y\y ，在第y\y 列左边添加一列。
5.输入x\x 、y\y ，查找坐标为(x,y)\(x,y) 的单元格的值。
请编写程序，判断对表格的各种操作是否合法。
"""
while True:
    try:
        # 初始化
        m, n = map(int, input().split())
        if m > 9 or n > 9:
            print('-1')
        else:
            print('0')
        
        # 交换坐标
        x1, y1, x2, y2 = map(int, input().split())
        if 0 <= x1 < m and 0 <= x2 < m and 0 <= y1 < n and 0 <= y2 < n:
            print('0')
        else:
            print('-1')
        
        # 插入行
        x = int(input())
        if m < 9 and 0 <= x < m:
            print('0')
        else:
            print('-1')
        
        # 插入列
        y = int(input())
        if n < 9 and 0 <= y < n:
            print('0')
        else:
            print('-1')
        
        # 查找坐标
        x, y = input().split()
        x, y = int(x), int(y)
        if 0 <= x < m and 0 <= y < n:
            print('0')
        else:
            print('-1')
    except:
        break 
