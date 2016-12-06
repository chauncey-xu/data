#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = 'ip1.txt'
with open(filename,"r") as f :
    host_list = f.read().splitlines()


def whois(host):
    """
    查找 host 的 whois 信息
    :param host: 需要查找的 host, 字符串
    :return: whois 信息, 字典
    """
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # 定义 socket 参数

    buf = ""                                                      # 创建 'buf' 的字符串

    try:
        s.connect(("whois.arin.net", 43))                         #建立 socket 连接,'whois.arin.net',端口:43
        s.send(bytes("n + {}\r\n".format(host), "utf-8"))         #发送 socket 数据,'format'函数是讲内容带入到文本中

        while True:                                               # 每次获取1024字节的结果,直到 recv 返回内容为空时,关闭 socket 连接;
            r = s.recv(1024)
            if r:
                buf += r.decode("utf-8")                          #'decode'将内容转换成 utf-8 的编码展示;
            else:
                s.close()
                break
    except Exception as e:
        print(e)                                                  #捕获错误信息,将错误信息输出

    data = dict()                                                 #创建'data'字典;
    for line in buf.splitlines():                                 #每行读取'buf'的数据,每行定义为'line';
        if line == "" or line.startswith("#") or line.startswith("Comment"):                 #如果'line'的起始为'#'或'Comment'话,跳过该行;
            continue

        if ": " in line:                                          #如果': ' 在 'line' 中,
            strings = line.split(": ")                            #以': '为分割点,
            key = strings[0].strip()                              #将分割后的第一个内容([0])赋值给 key
            value = "".join(strings[1:]).strip()                  #分割后的剩余所有内容([1:]),赋值给 value;
            data[key] = value                                     #将 key 和 value 的内容关联起来

    return data                                                   #向主程序,返回'data'字典;


def excel(result):
    
#    keys = ["Host", "NetRange", "NetName", "OrgName", "Country","OrgAbuseEmail","RTechEmail"]    #建立'keys'列表,赋值为所有需要的信息
    keys = ["Host", "NetRange", "NetName", "Organization", "Country","OrgTechEmail","RTechEmail"]    #建立'keys'列表,赋值为所有需要的信息

    file = open("whois_result.csv", "w")    #打开 CSV 文件;
    file.write(",".join(keys) + "\n")       #将 keys 中的所有信息,输入到第一行中;
    for result in result_list:
        result['Organization'] = result['Organization'].replace(',','|',10)
        line = ""
        for key in keys:
            line += result.get(key, "") + ","
            
        file.write(line + "\n")

    file.close()

    return 

if __name__ == "__main__":


    result_list = list()               #创建'result_list'的 list;

    for host in host_list:             #每行读取 host_list,定义每行为 host;
        result = whois(host)           #调用 whois 函数,结果定义为 result;
#        print(result)
        if result == {}:
            result["Host"] = host
            print (result,'/////')
#            pass
        else:
            result["Host"] = host          #将'host' 内容赋值到 result 列表的 'host' 中;        
            result_list.append(result)     #将 result 中的信息追加到'result_list'列表中;
            excel(result)                  #调用 excel 函数，将结果追加到 CSV 文件中;