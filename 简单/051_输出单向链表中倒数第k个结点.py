"""
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。
"""
while True:
    try:
        lens = int(input())
        n_list = input().split()
        index = int(input())
        if index == 0:
            print(0)
        else:
            print(n_list[-1 * index])
    except:
        break