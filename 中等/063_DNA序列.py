"""
一个 DNA 序列由 A/C/G/T 四个字母的排列组合组成。 G 和 C 的比例（定义为 GC-Ratio ）是序列中 G 和 C 两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的 GC-Ratio 可能是基因的起始点。
给定一个很长的 DNA 序列，以及限定的子串长度 N ，请帮助研究人员在给出的 DNA 序列中从左往右找出 GC-Ratio 最高且长度为 N 的第一个子串。
DNA序列为 ACGT 的子串有: ACG , CG , CGT 等等，但是没有 AGT ， CT 等等
"""
while True:
    try:
        jy_str = input()
        jy_num = int(input())
        res_list = []
        for i in range(len(jy_str)-jy_num + 1):
            res_list.append(jy_str[i:i+jy_num])
        GC_Ratio_list = []
        for res in res_list:
            G_count = res.count("G")
            C_count = res.count("C")
            GC_Ratio = (G_count + C_count)/len(res)
            GC_Ratio_list.append(GC_Ratio)
        MAX_count = max(GC_Ratio_list)
        print(res_list[GC_Ratio_list.index(MAX_count)])
    except:
        break