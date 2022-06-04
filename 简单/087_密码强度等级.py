"""
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
"""

while True:
    try:
        scores = 0
        s = input()
        # 长度校验
        if len(s) <= 4:
            scores += 5
        elif 5 <= len(s) <= 7:
            scores += 10
        elif len(s) >= 8:
            scores += 25
            
        w_uper= 0
        w_lower= 0
        num = 0
        signal =0
        for i in s:
            if i.islower():
                w_lower += 1
            elif i.isupper():
                w_uper += 1
            elif i.isalnum():
                num += 1
            else:
                signal += 1
                
        if w_lower == 0 and w_uper == 0:
            scores += 0
        elif w_lower !=0 and w_uper != 0:
            scores += 20
        else:
            scores += 10
            
        if num == 0:
            scores += 0
        elif num == 1:
            scores += 10
        elif num > 1:
            scores += 20
            
        if signal == 0:
            scores += 0
        elif signal == 1:
            scores += 10
        elif signal > 1:
            scores += 25
        # 奖励
        if  w_lower !=0 and w_uper != 0 and num !=0 and signal !=0:
            scores += 5
        elif num !=0 and signal !=0 and (w_lower !=0 or w_uper != 0):
            scores += 3
        elif num !=0 and (w_lower !=0 or w_uper != 0):
            scores += 2
        
        if scores >= 90:
            print('VERY_SECURE')
        elif scores >= 80:
            print('SECURE')
        elif scores >= 70:
            print('VERY_STRONG')
        elif scores >= 60:
            print('STRONG')
        elif scores >= 50:
            print('AVERAGE')
        elif scores >= 25:
            print('WEAK')
        else:
            print('VERY_WEAK')
    except:
        break