def rect(a,b,disp):
    for i in range(b):
        disp[i] = '#'*a+disp[i][a:]
    return disp

def rotate_row(y,a,disp):
    disp[y] = disp[y][len(disp[y])-a:]+disp[y][:len(disp[y])-a]
    return disp

def rotate_column(x,a,disp):
    col = []
    disp0 = []
    for d in disp:
        col.append(d[x])
    for i in range(len(disp)):
        dl = list(disp[i])
        dl[x] = col[(i-a)%len(disp)]
        disp0.append(''.join(dl))
    return disp0

def rotate(direction,xy,a,disp):
    if direction == 'row':
        return rotate_row(xy,a,disp)
    return rotate_column(xy,a,disp)

def show(disp):
    for d in disp:
        print d.replace('.',' ')

def d8_1():
    disp = ['.'*50]*6
    lit = 0
    with open('day08.input','r') as data:
        for d in data:
            cmd = d.split()
            if cmd == []:
                continue
            if cmd[0] == 'rect':
                a,b = cmd[1].split('x')
                disp = rect(int(a),int(b),disp)
            elif cmd[0] == 'rotate':
                disp = rotate(cmd[1],int(cmd[2].split('=')[1]),int(cmd[4]),disp)
    for d in disp:
        lit += d.count('#')
    print "Number of pixels lit:",lit
    show(disp)

if __name__ == '__main__':
    d8_1()
