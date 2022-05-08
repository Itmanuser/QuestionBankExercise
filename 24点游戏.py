import itertools

card_dict = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}

def func(a,b,c,d):
    a1,b1,c1,d1 = card_dict[a],card_dict[b],card_dict[c],card_dict[d]
    rules = ['+',"-","*","/",'+',"-","*","/",'+',"-","*","/"]
    all_rules = itertools.permutations(rules,3)
    for x,y,z in all_rules:
        result = eval("((({}{}{}){}{}){}{})".format(a1,x,b1,y,c1,z,d1))
        if result == 24 or result == 24.0:
            return "{}{}{}{}{}{}{}".format(a,x,b,y,c,z,d)


if __name__ == '__main__':
    n = ["5","7","3","9"]
    if "joker" in n or 'JOKER' in n:
        print("ERROR")
    else:
        res_list = []
        all_range = itertools.permutations(n,4)
        for one_range in all_range:
            a,b,c,d = one_range
            res = func(a,b,c,d)
            if res:
                res_list.append(res)
        if res_list:
            print(res_list[0])
        else:
            print("NONE")