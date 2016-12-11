import collections

def d6_1():
    signal = ['','','','','','','','']
    with open('day6.input','r') as data:
        for d in data:
            for i in range(8):
                signal[i] += d[i]
    msg = []
    for s in signal:
        msg.append(collections.Counter(s).most_common(1)[0][0])
    print "Error corrected message #1:",''.join(msg)

def d6_2():
    signal = ['','','','','','','','']
    with open('day6.input','r') as data:
        for d in data:
            for i in range(8):
                signal[i] += d[i]
    msg = []
    for s in signal:
        msg.append(collections.Counter(s).most_common()[-1][0])
    print "Error corrected message #2:",''.join(msg)

if __name__ == '__main__':
    d6_1()
    d6_2()
