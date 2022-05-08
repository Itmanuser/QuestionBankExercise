yuan = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']

def ch(s):
    res = ''
    if len(s) == 4:
        if s[0] != '0':
            res += yuan[int(s[0])] + '仟'
        else:
            if s[1] != '0':
                res += yuan[int(s[0])]
        if s[1] != '0':
            res += yuan[int(s[1])] + '佰'
        else:
            if s[2] != '0':
                res += yuan[int(s[1])]
        if s[2] != '0':
            if s[2] != '1':
                res += yuan[int(s[2])] + '拾'
            else:
                res += '拾'
        else:
            if s[3] != '0':
                res += yuan[int(s[2])]
        if s[3] != '0':
            res += yuan[int(s[3])]
    elif len(s) == 3:
        if s[0] != '0':
            res += yuan[int(s[0])] + '佰'
        else:
            res += yuan[int(s[0])]
        if s[1] != '0':
            if s[1] != '1':
                res += yuan[int(s[1])] + '拾'
            else:
                res += '拾'
        else:
            res += yuan[int(s[1])]
        if s[2] != '0':
            res += yuan[int(s[2])]
    elif len(s) == 2:
        if s[0] != '0':
            if s[0] != '1':
                res += yuan[int(s[0])] + '拾'
            else:
                res += '拾'
        else:
            res += yuan[int(s[0])]
        if s[1] != '0':
            res += yuan[int(s[1])]
    elif len(s) == 1:
        if s[0] != '0':
            res += yuan[int(s[0])]
    return res


def handle_after(after):
    if len(after) < 3:
        if len(after) == 2: 
            if after == "00":
                after = "整"
            else:
                if after[0] == "0" and after[1] != "0":
                    after = "{}分".format(yuan[int(after[1])])
                elif after[1] == "0" and after[0] != "0":
                    after = "{}角".format(yuan[int(after[0])])
                else:
                    after = "{}角{}分".format(yuan[int(after[0])], yuan[int(after[1])])
        elif len(after) == 1:
            after = "{}角".format(yuan[int(after[0])])
        return after
    
def handle_befor(befor):
    res1, res2 = "", ""
    if len(befor) > 8:
        res1 += ch(befor[:-8]) + '亿'
        res1 += ch(befor[-8:-4]) + '万'
        res2 += ch(befor[-4:])
    elif len(befor) > 4:
        res1 += ch(befor[:-4]) + '万'
        res2 += ch(befor[-4:])
    else:
        res2 += ch(befor)
    if befor == "0":
        return res1 + res2
    else:
       return res1 + res2 + "元" 
    
if __name__ == '__main__':
    # n = input()
    n = "1233.1"
    [befor,after] = n.split(".")
    befors = handle_befor(befor)
    afters = handle_after(after)
    print("人民币{}{}".format(befors,afters))