"""
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
"""

def handle_res(res_list):
    res_list = list(filter(lambda x: (len(x) == 3 or len(x) == 2), res_list))
    result = []
    for res in res_list:
        if res.startswith("A") or res.startswith("D") or res.startswith("W") or res.startswith("S"):
            try:
                int(res[1:])
                result.append(res)
            except:
                pass
    return result

while True:
    try:
        x, y = 0,0
        res_list = input().split(";")
        result = handle_res(res_list)
        for res in result:
            if res.startswith("A"):
                x = x - int(res[1:])
            elif res.startswith("D"):
                x = x + int(res[1:])
            elif res.startswith("W"):
                y = y + int(res[1:])
            elif res.startswith("S"):
                y = y - int(res[1:])
        print("{},{}".format(x,y))
                
    except:
        break