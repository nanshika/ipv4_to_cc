# python %google_drive_path%\Script\ipv4_to_cc\search_cc.py 1.1.1.1
# -*- coding: utf-8 -*-
# IPアドレスからCountry Codeを取得する
import sys
import re
import pandas as pd


def search_cc(input_ip):
    with open('ip_list.csv', 'r') as f:
        for l in f.readlines():
            (ip_s, ip_e, cc) = l.rstrip().split(',')
            
            if input_ip in range(int(ip_s), int(ip_e)+1):
                
                # IPv4形式に戻すために計算
                i0 = (input_ip >> 24)
                i1 = (input_ip >> 16) - 256 * i0
                i2 = (input_ip >> 8 ) - 256**2 * i0 - 256    * i1
                i3 =  input_ip        - 256**3 * i0 - 256**2 * i1 - 256 * i2
                i9 = str(i0) + '.' + str(i1) + '.' + str(i2) + '.' + str(i3)
                
                with open('cc2name.tsv', 'r') as f:
                    cc2name_df = pd.read_csv(f, delimiter='\t')
                
                for i, values in cc2name_df.iterrows():
                    if cc == values['cc']:
                        cc_name = values['name']
                
                print('tar_ip: ' + i9 +' ('+ str(input_ip) +  ')\tcc: ' + cc + ' (' + cc_name + ')')
                return(cc)

def main():
    if len(sys.argv) != 2:
        print('Set only one arg for this script!\n')
        exit()
    
    input_ip = sys.argv[1]
    if re.match('\d+$', str(input_ip)):
        pass
    elif re.search('\d*\.\d*\.\d*\.\d*', input_ip):
        i = input_ip.split('.')
        input_ip = (int(i[0]) << 24) + (int(i[1]) << 16) + (int(i[2]) << 8) + int(i[3])
    else:
        print('Invalid arg!\n')
        exit()
    
    search_cc(int(input_ip))

main()
 