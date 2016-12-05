def d1():
    input = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"
    ia = input.split(", ")
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
        print cd, '->', p
    print p
    print abs(p[0])+abs(p[1])

def d2():
    input = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"
    ia = input.split(", ")
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
            print c[d], '->', p
            if p in pos:
                print 'Visited before:',p
                done = True
                break
            pos.append(p)
    print p
    print abs(p[0])+abs(p[1])

if __name__ == '__main__':
	d2()
