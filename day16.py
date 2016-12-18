def generate_checksum(data):
    while True:
        pairs = [data[i:i+2] for i in range(0, len(data), 2)]
        chksum = ''
        for p in pairs:
            if p[0] == p[1]:
                chksum += '1'
            else:
                chksum += '0'
        if len(chksum) % 2 == 0:
            data = chksum
        else:
            break
    return chksum

def generate_data(a,size):
    while len(a) < size:
        b = a[::-1]
        b = b.replace('0','a')
        b = b.replace('1','0')
        b = b.replace('a','1')
        a = a + '0' + b
    return a[:size]

def d16_2():
    data = '01111001100111011'
    disk = 35651584
    data = generate_data(data,disk)
    chksum = generate_checksum(data)
    print 'The generated checksum is #2:',chksum

def d16_1():
    data = '01111001100111011'
    disk = 272
    data = generate_data(data,disk)
    chksum = generate_checksum(data)
    print 'The generated checksum is #1:',chksum

if __name__ == '__main__':
    d16_1()
    d16_2()
    
