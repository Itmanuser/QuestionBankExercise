"""
输入描述：
多行字符串，每行字符串一条命令
输出描述：
执行结果，每条命令输出一行
"""

while True:
    try:
        m = input().strip().split()
        key = ["reset board", "reset", "board add", "board delete", "reboot backplane", "backplane abort"]
        value = ["board fault", "reset what", "where to add", "no board at all", "impossible", "install first"]
        if len(m) < 1 or len(m) > 2:
            print("unknown command")
        elif len(m) == 1:  # 当输入一个字符串
            find_it = False
            for i in range(len(key)):
                if len(key[i].split()) == 1 and m[0] == key[i][:len(m[0])]:
                    print(value[i])
                    find_it = True
                    break  # 找到了就跳出循环
            if not find_it:
                print("unknown command")  # 都没有找到就是 unknown
        else:
            index = []
            for i in range(len(key)):
                a = key[i].split()  # 将具体的一个 key 分割成两部分
                if len(a) != 1 and m[0] == a[0][:len(m[0])] and m[1] == a[1][:len(m[1])]:  # 去匹配被分割的 key
                    index.append(i)  # 符合条件就把这个位置放入列表
            if len(index) != 1:
                print("unknown command")
            else:
                print(value[index[0]])  # 输出对应的value值
    except:
        break

