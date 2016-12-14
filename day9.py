import re

def decompressed_length_2(data):
    if not re.findall('[(]+',data):
        length = len(data)
    else:
        a,b,c,d = re.findall('(.*?)\(([0-9]+)x([0-9]+)\)(.*)',data)[0]
        length = len(a) + int(c)*decompressed_length_2(d[:int(b)]) + decompressed_length_2(d[int(b):])
    return length

def d9_1():
    with open('day9.input','r') as d:
        data = d.read()
    not_done = True
    length = 0
    while not_done:
        if not re.findall('[(]+',data):
            not_done = False
            length += len(data)
        else:
            a,b,c,d = re.findall('(.*?)\(([0-9]+)x([0-9]+)\)(.*)',data)[0]
            length += len(a) + int(b)*int(c)
            data = d[int(b):]
    print "Decompressed length of file #1:",length

def d9_2():
    with open('day9.input','r') as d:
        data = d.read()
    length = decompressed_length_2(data)
    print "Decompressed length of file #2:",length

if __name__ == '__main__':
    d9_1()
    d9_2()
