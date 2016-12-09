import collections

def d4_1():
    with open('day4.input','r') as data:
        total_sec = 0
        for d in data:
            enc = d.rsplit('-',1)[0].replace('-','')
            sec = d.rsplit('-',1)[1].split('[')[0]
            chk = d.split('[')[1].split(']')[0]
            letters = collections.Counter(enc).most_common()
            chk0 = ''
            num = 0
            for l in letters:
                if num == 0:
                    cur = [l[0]]
                    num = l[1]
                elif num == l[1]:
                    cur.append(l[0])
                else:
                    cur.sort()
                    chk0 += ''.join(cur)
                    cur = [l[0]]
                    num = l[1]
            cur.sort()
            chk0 += ''.join(cur)
            if chk0[0:len(chk)] == chk:
                total_sec += int(sec)

    print "Total sector ID sum of real rooms:",total_sec

def d4_2():
    with open('day4.input','r') as data:
        for d in data:
            enc = d.rsplit('-',1)[0]
            sec = d.rsplit('-',1)[1].split('[')[0]
            chk = d.split('[')[1].split(']')[0]
            data = []
            for c in enc:
                if c == '-':
                    data.append(' ')
                else:
                    data.append(chr(((ord(c)-97+int(sec))%26)+97))
            out = ''.join(data)
            if 'north' in out:
                print 'Sector ID of room with text \''+out+'\'', sec

if __name__ == '__main__':
    d4_1()
    d4_2()
