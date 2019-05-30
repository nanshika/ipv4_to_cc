# python get_AS_info.py
# -*- coding: utf-8 -*-
#
import requests, urllib, hashlib, os, re, subprocess, datetime, time, random
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import ipaddress
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3538.9 Safari/537.36' }
home_path = ''

def decimalip_range(ip_net):
    ip_s = str(ipaddress.ip_network(ip_net)[0])
    ip_e = str(ipaddress.ip_network(ip_net)[-1])
    i = ip_s.split('.')
    deci_ip_s = (int(i[0]) << 24) + (int(i[1]) << 16) + (int(i[2]) << 8) + int(i[3])
    i = ip_e.split('.')
    deci_ip_e = (int(i[0]) << 24) + (int(i[1]) << 16) + (int(i[2]) << 8) + int(i[3])
    return(str(deci_ip_s) + '\t' + str(deci_ip_e))


f_out2 = open('jp_AS.tsv','a', encoding='sjis')
f_err2 = open('jp_AS_err.tsv','a', encoding='sjis')

url = 'https://ipinfo.io/countries/jp'
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.content,'lxml')
domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
try:
    for a in soup.table.find_all('a'):
        url = domain + a.get('href')
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.content,'lxml')
        title = soup.title.text.replace(' - IPinfo IP Address Geolocation API','')
        print(url)
        for a2 in soup.find('tbody',{'class':'t-14'}).find_all('a'):
            ip_range = decimalip_range(re.sub('[ |\n]+','', a2 .text))
            out = title + '\t' + ip_range
            f_out2.write(out + '\n')
    time.sleep(1)
except:
    f_err2.write(url + '\n')
    
#for url in AS_list:
#    res = requests.get(url,headers=headers)
#    soup = BeautifulSoup(res.content,'lxml')
#    title = soup.title.text.replace(' - IPinfo IP Address Geolocation API','')
#    try:
#    for a2 in soup.find('tbody',{'class':'t-14'}).find_all('a'):
#        out = title + '\t'+ re.sub('[ |\n]+','', a2 .text)
