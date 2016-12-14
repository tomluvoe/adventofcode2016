import hashlib

def d5_1():
    data = "ugkcyxxp"
    passwd = []
    idx = 0
    while len(passwd) < 8:
        h = hashlib.md5(data+str(idx)).hexdigest()
        if h[0:5] == '00000':
            print h
            passwd.append(h[5])
        idx += 1
    print "Password #1:",''.join(passwd)

def d5_2():
    data = "ugkcyxxp"
    passwd = ['_','_','_','_','_','_','_','_']
    idx = 0
    not_done = True
    while not_done:
        h = hashlib.md5(data+str(idx)).hexdigest()
        if h[0:5] == '00000':
            if h[5].isdigit() and int(h[5]) < 8:
                if passwd[int(h[5])] == '_':
                    passwd[int(h[5])] = h[6]
        if '_' not in passwd:
            not_done = False
        if idx%1000000 == 0:
            print ''.join(passwd)
        idx += 1
    print "Password #2:",''.join(passwd)

if __name__ == '__main__':
    d5_1()
    d5_2()
