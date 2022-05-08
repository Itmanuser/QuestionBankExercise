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