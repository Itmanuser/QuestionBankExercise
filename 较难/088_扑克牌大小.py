dic = {'3' : 1, '4' : 2, '5' : 3, '6' : 4, '7' : 5, '8': 6,
        '9' : 7, '10' : 8, 'J' : 9, 'Q' : 10, 'K' : 11, 'A' : 12,
        '2' : 13, 'joker' : 14, 'JOKER' : 15}

while True:
    try:
        s1, s2 = input().split('-')
        list1, list2 = s1.split(), s2.split()
        L1, L2 = len(list1), len(list2)
        if L1 == L2:
            if dic[list1[0]] > dic[list2[0]]:
                print(s1)
            else:
                print(s2)
        else:
            if "joker JOKER" == s1 or "joker JOKER" == s2:
                print("joker JOKER")
            elif list1.count(list1[0]) == 4:
                print(s1)
            elif list2.count(list2[0]) == 4:
                print(s2)
            elif list1.count(list1[0]) == 4 and list1.count(list2[0]) == 4:
                if list1[0] > list2[0]:
                    print(s1)
                else:
                    print(s2)
            else:
                print("ERROR")
    except:
        break