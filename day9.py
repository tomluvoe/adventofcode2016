import re

def decompressed_length_2(data):
    if not re.findall('[(]+',data):
        length = len(data)
    else:
        parsed = re.findall('(.*?)\(([0-9]+)x([0-9]+)\)(.*)',data)
        print data
        a,b,c,d = parsed[0]
        print int(b),int(c),'!!',d
        length = len(a) + int(b)*decompressed_length_2(d[:int(c)+1])# + decompressed_length_2()
    return length

def decompressed_length(data):
    if not re.findall('[(]+',data):
        length = len(data)
    else:
        parsed = re.findall('(.*?)\(([0-9]+)x([0-9]+)\)(.*)',data)
        a,b,c,d = parsed[0]
        #length = len(a) + int(b)*int(c) + decompressed_length(d[int(b):])
        length = len(a) + decompressed_length_2(d[:int(b)]*int(c)) + decompressed_length(d[int(b):])
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
            parsed = re.findall('(.*?)\(([0-9]+)x([0-9]+)\)(.*)',data)
            a,b,c,d = parsed[0]
            length += len(a) + int(b)*int(c)
            data = d[int(b):]
    print "Decompressed length of file #1:",length

def d9_2():
    with open('day9.input','r') as d:
        data = d.read()
    data = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    length = decompressed_length_2(data)
    print "Decompressed length of file #2:",length

if __name__ == '__main__':
    d9_1()
    #d9_2()
