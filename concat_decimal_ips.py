# python concat_decimal_ips.py
def concat_decimal_ips(list1):
    f_out = open('jp_AS_mod2.tsv', 'w', encoding='sjis')
    list2 = []
    ip_st1 = ''
    ip_en1 = ''
    firm1 = '\n'
    for l in sorted(list1):
        (ip_st2, ip_en2, firm2) = l.split('\t')
        if firm1 == firm2 and int(ip_st2) <= int(
                ip_st1) and int(ip_en1) <= int(ip_en2):
            # 上の行のレンジに含まれる
            # print('Included! ' + ip_st2 + '<=' + ip_st1 + '<=' + ip_en1 + '<=' + ip_en1 + '\t' + firm2)
            pass
        elif firm1 == firm2 and int(ip_en1) + 1 == int(ip_st2):
            # 連続するIPのため結合
            # print('Concat! ' + ip_st1 + '<=' + ip_st2 + '<=' + ip_en2 + '<=' + ip_en2 + '\t' + firm2)
            ip_en1 = ip_en2
        else:
            if ip_st1 != '':
                ip_firm = ip_st1 + '\t' + ip_en1 + '\t' + firm1
                _ = f_out.write(ip_firm)
                list2.append(ip_firm)
            firm1 = firm2
            ip_st1 = ip_st2
            ip_en1 = ip_en2
    ip_firm = ip_st1 + '\t' + ip_en1 + '\t' + firm1
    _ = f_out.write(ip_firm)
    list2.append(ip_firm)
    f_out.close()
    return(list2)


f_in = open('jp_AS_mod.tsv', 'r', encoding='sjis')
concat_decimal_ips(f_in.readlines())
