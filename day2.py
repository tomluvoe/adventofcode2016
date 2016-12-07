def d2_1():
    pad = "123456789"
    pos = 4
    mv = {"R": [1,1,0,1,1,0,1,1,0], "L": [0,-1,-1,0,-1,-1,0,-1,-1], "U": [0,0,0,-3,-3,-3,-3,-3,-3], "D": [3,3,3,3,3,3,0,0,0]}
    code = ''
    with open('day2.input','r') as data:
        for d in data:
            for c in d.rstrip():
                pos += mv[c][pos]
            code += pad[pos]
    print "Code #1:", code

def d2_2():
    pad = "123456789ABCD"
    pos = 4
    mv = {"R":[0,1,1,0,1,1,1,1,0,1,1,0,0], "L": [0,0,-1,-1,0,-1,-1,-1,-1,0,-1,-1,0], "U": [0,0,-2,0,0,-4,-4,-4,0,-4,-4,-4,-2], "D": [2,4,4,4,0,4,4,4,0,0,2,0,0]}
    code = ''
    with open('day2.input','r') as data:
        for d in data:
            for c in d.rstrip():
                pos += mv[c][pos]
            code += pad[pos]
    print "Code #2:", code

if __name__ == "__main__":
    d2_1()
    d2_2()
