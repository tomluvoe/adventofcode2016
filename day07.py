import re

def has_abba(data):
    for d in data:
        if len(d) < 4:
            continue
        for i in range(len(d)-3):
            if d[i] == d[i+3] and d[i+1] == d[i+2] and d[i] != d[i+1]:
                return True
    return False

def find_aba(data):
    aba = []
    for d in data:
        if len(d) < 3:
            continue
        for i in range(len(d)-2):
            if d[i] == d[i+2] and d[i] != d[i+1]:
                aba.append(d[i:i+3])
    return aba

def find_bab(data,aba):
    if len(aba) < 1:
        return False
    for a in aba:
        for d in data:
            if len(d) < 3:
                continue
            for i in range(len(d)-2):
                if d[i] == d[i+2] and d[i] == a[1] and d[i+1] == a[0]:
                    return True
    return False

def parse_data(data,brackets):
    if brackets == 'in':
        return re.findall('\[(.*?)\]',data)
    else:
        return re.findall('^(.*?)\[',data) +\
               re.findall('\]([^[]+?)$',data) +\
               re.findall('\](.*?)\[',data)

def d7_1():
    supported = 0
    with open('day07.input','r') as data:
        for d in data:
            if not has_abba(parse_data(d,'in')) and \
                has_abba(parse_data(d,'out')):
                supported += 1
    print "IPs supporting TLS:",supported

def d7_2():
    supported = 0
    with open('day07.input','r') as data:
        for d in data:
            aba = find_aba(parse_data(d,'out'))
            if find_bab(parse_data(d,'in'),aba):
                supported += 1
    print "IPs supporting SSL:",supported

if __name__ == '__main__':
    d7_1()
    d7_2()
