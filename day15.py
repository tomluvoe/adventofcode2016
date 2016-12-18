import re

def solve_discs(discs):
    not_found = True
    time = 0
    while not_found:
        pos_sum = 0
        for i,d in enumerate(discs):
            pos, num_pos = d
            now_pos = (pos + time + i + 1) % num_pos
            pos_sum += now_pos
        if pos_sum == 0:
            not_found = False
            break
        time += 1
    return time

def d15_1():
    discs = []
    with open('day15.input','r') as data:
        for d in data:
            match = re.findall('Disc #(\w+?) has (\w+?) .* time=(\w+?), .* (\w+?).$',d)[0]
            discs.append([int(match[3]),int(match[1])])
    time = solve_discs(discs)
    print 'The first time you can press a button to get a capsule #1 is at:',time

def d15_2():
    discs = []
    with open('day15.input','r') as data:
        for d in data:
            match = re.findall('Disc #(\w+?) has (\w+?) .* time=(\w+?), .* (\w+?).$',d)[0]
            discs.append([int(match[3]),int(match[1])])
    discs.append([0,11])
    time = solve_discs(discs)
    print 'The first time you can press a button to get a capsule #2 is at:',time

if __name__ == '__main__':
    d15_1()
    d15_2()
