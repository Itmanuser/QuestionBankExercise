"""
“兄弟单词”：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。
"""
while True:
    try:
        n = input().split()
        num = int(n[0])
        word_list = n[1:num+1]
        key_word = n[-2]
        k = int(n[-1])
        res_list = []
        for word in word_list:
            if word != key_word:
                if sorted(word) == sorted(key_word):
                    res_list.append(word)
        result = sorted(res_list)
        print(len(result))
        print(result[k-1])
    except:
        break