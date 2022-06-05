"""1 总体说明
考生需要模拟实现一个简单的自动售货系统，实现投币、购买商品、退币、查询库存商品及存钱盒信息的功能。
系统初始化时自动售货机中商品为6种商品,商品的单价参见1.1规格说明，存钱盒内放置1元、2元、5元、10元钱币，商品数量和钱币张数通过初始化命令设置，参见2.1 系统初始化。
1.1规格说明
1. 商品:每种商品包含商品名称、单价、数量三种属性，其中商品名不重复。考生不能修改商品名称和单价，初始化命令设置商品数量。这些信息在考试框架中进行定义，考生在实现功能代码时可直接使用。
"""
while True:
    try:
        a = input().split(';')
        coin = 0 #存储余额
        commodity_list = {'A1':[2],'A2':[3],'A3':[4],'A4':[5],'A5':[8],'A6':[6]} #初始化商品字典，列表中为商品单价
        balance_list = {'1':0,'2':0,'5':0,'10':0} #初始化存钱盒
        inita = a[0].split() #初始化的语句，以空格分开字符串
        inita_com = list(map(int,inita[1].split('-'))) #初始化商品部分，按‘-’分开
        commodity_list['A1'].append(inita_com[0]) #六种商品一一初始化他们的初始数量
        commodity_list['A2'].append(inita_com[1])
        commodity_list['A3'].append(inita_com[2])
        commodity_list['A4'].append(inita_com[3])
        commodity_list['A5'].append(inita_com[4])
        commodity_list['A6'].append(inita_com[5])
        inita_bal = list(map(int,inita[2].split('-'))) #初始化存钱盒部分
        balance_list['1'] += inita_bal[0] #四种面额的钱一一初始化
        balance_list['2'] += inita_bal[1]
        balance_list['5'] += inita_bal[2]
        balance_list['10'] += inita_bal[3]
        print('S001:Initialization is successful') #输出初始化成功语句
        for i in range(1,len(a) - 1): #输入的语句一一作出操作，因为输入的最后一天字符是‘；’所以a的最后一项是空，要去掉
            if(a[i][0] == 'p'): #投钱
                input_coin = int(a[i][2:]) #投钱的数目
                coin_all_1_2 = 1 * balance_list['1'] + 2 * balance_list['2'] #1元和2元面额的钱的总额度
                all_com_num = 0 #所有的商品总量
                for key,value in commodity_list.items(): #计算所有商品的总数量
                    all_com_num += value[1]
                if(input_coin != 1) and (input_coin != 2) and (input_coin != 5) and (input_coin != 10): #如果投的钱不为1，2，5，10
                    print('E002:Denomination error')
                elif(input_coin > coin_all_1_2): #投的钱比一元和二元总额度大
                    if(input_coin == 1) or (input_coin == 2): #一元二元不受此限制
                        coin += input_coin #余额加
                        balance_list[str(input_coin)] += 1 #放入对应存钱盒
                        print('S002:Pay success,balance=' + str(coin)) 
                    else:
                        print('E003:Change is not enough, pay fail')
                elif(all_com_num == 0): #商品总数为0
                    print('E005:All the goods sold out')
                else: #否则正常输出
                    coin += input_coin
                    balance_list[str(input_coin)] += 1
                    print('S002:Pay success,balance=' + str(coin))
            if(a[i][0] == 'b'):#买东西
                need_goods = a[i][2:]
                if(need_goods not in commodity_list): #不在商品列表中
                    print('E006:Goods does not exist')
                elif(commodity_list[need_goods][1] == 0): #存量为0
                    print('E007:The goods sold out')
                elif(coin < commodity_list[need_goods][0]): #钱不够
                    print('E008:Lack of balance')
                else: #正常够买
                    commodity_list[need_goods][1] -= 1 #存量减一
                    coin -= commodity_list[need_goods][0] #余额减
                    print('S003:Buy success,balance=' + str(coin))
            if(a[i][0] == 'c'): #退钱
                if(coin == 0):
                    print('E009:Work failure')
                else:
                    need_back = [0,0,0,0] #四张面额应退的数量
                    while coin >= 0: #余额大于0
                        if(coin >= 10) and (balance_list['10'] != 0): #大于10且存钱盒有10元
                            coin -= 10
                            balance_list['10'] -= 1
                            need_back[3] += 1
                        elif(coin >= 5) and (balance_list['5'] != 0):#大于5且存钱盒有5元
                            coin -= 5
                            balance_list['5'] -= 1
                            need_back[2] += 1
                        elif(coin >= 2) and (balance_list['2'] != 0):#大于2且存钱盒有2元
                            coin -= 2
                            balance_list['2'] -= 1
                            need_back[1] += 1
                        elif(coin >= 1) and (balance_list['1'] != 0):#大于1且存钱盒有1元
                            coin -= 1
                            balance_list['1'] -= 1
                            need_back[0] += 1
                        else:#到这里，只有余额为零或者剩余的钱已经无法退回
                            coin = 0 #余额清零
                            print('1 yuan coin number=' + str(need_back[0]))
                            print('2 yuan coin number=' + str(need_back[1]))
                            print('5 yuan coin number=' + str(need_back[2]))
                            print('10 yuan coin number=' + str(need_back[3]))
                            break
            if(a[i][0] == 'q'): #查询
                if(a[i] == 'q 0'): #必须是q 0,q 1，才能查询；q0不合法
                    for key,value in commodity_list.items():
                        print(key + str(value[0]) + str(value[1]))
                elif(a[i] == 'q 1'):
                    for key,value in balance_list.items():
                        print(key + ' yuan coin number=' + str(value))
                else:
                    print('E010:Parameter error')
    except:
        break
