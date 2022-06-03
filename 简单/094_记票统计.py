""""
请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。
"""

while True:
    try:
        p_num = int(input())
        name = input().split()
        m = int(input())
        t_name = input().split()
        res_dict = {}
        for i in name:
            res_dict[i] = t_name.count(i)
            
        vailed = 0
        for k,v in res_dict.items():
            vailed += v
            print(k,":",v)
        print("Invalid",":",m-vailed)
    except:
        break 
    