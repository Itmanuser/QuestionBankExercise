"""
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是“相同”的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。也就是说，哪怕不同路径下的文件，如果它们的名字的后16个字符相同，也被视为相同的错误记录
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
"""
import sys

paths_list = []
path_dict = {}
while True:
    try:
        paths = input()
        paths_list.append(paths)
    except:
        break
        
for paths in paths_list:
    path, line = paths.split(" ")
    name = path.split("\\")[-1]
    if len(name) > 16:
        name = name[-16:]
    if (name, line) not in path_dict.keys():
        path_dict[(name, line)] = 1
    else:
        path_dict[(name, line)] = path_dict[(name, line)] + 1

for i, res in enumerate(path_dict.items()):
    if len(path_dict) -i > 8:
        continue
    else:
        print(res[0][0], res[0][1], res[1])