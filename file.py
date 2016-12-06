#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = 'ip.txt'
with open(filename,"r") as f :
    host_list = f.read().splitlines()

result = list()
for i in host_list:
    i = i.split('/')[0]
    result.append(i)

#data = result
#data1 = list()

#for i in data:
#    if i.endswith('0') is True:
#        result.append(i)
#    else:
#        #data1.append(i)
#        print(i)

for l in result:
    print (l)
