def d1_1():
    with open('day01.input','r') as data:
        indata = data.read()
    ia = indata.split(", ")
    p = [0,0]
    c = [[0,1],[1,0],[0,-1],[-1,0]]
    d0 = {"R": 1, "L": -1}
    d = 0
    pos = [p]
    for i in ia:
        d += d0[i[0]]
        d %= 4
        cd = [x * int(i[1:]) for x in c[d]]
        p = [sum(x) for x in zip(p, cd)]
    print "Distance #1:",abs(p[0])+abs(p[1])

def d1_2():
    with open('day01.input','r') as data:
        indata = data.read()
    ia = indata.split(", ")
    p = [0,0]
    c = [[0,1],[1,0],[0,-1],[-1,0]]
    d0 = {"R": 1, "L": -1}
    d = 0
    pos = [p]
    done = False
    for i in ia:
        if done == True:
            break
        d += d0[i[0]]
        d %= 4
        for x in range(int(i[1:])):
            p = [sum(x) for x in zip(p, c[d])]
            #print c[d], '->', p
            if p in pos:
                done = True
                break
            pos.append(p)
    print "Distance #2:", abs(p[0])+abs(p[1])

if __name__ == '__main__':
    d1_1()
    d1_2()
