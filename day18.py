def get_tile(l,c,r):
    if l == c and c != r or r == c and c != l:
        return '^'
    return '.'

def d18_2():
    with open('day18.input','r') as d:
        data = d.read()
    row = data.rstrip()
    safe = row.count('.')
    for i in range(400000-1):
        c_row = '.'+row+'.'
        next_row = ''
        for j in range(len(c_row)-2):
            l,c,r = c_row[j:j+3]
            next_row += get_tile(l,c,r)
        safe += next_row.count('.')
        row = next_row
    print 'The number of safe tiles is #2:',safe

def d18_1():
    with open('day18.input','r') as d:
        data = d.read()
    rows = [data.rstrip()]
    for i in range(39):
        c_row = '.'+rows[i]+'.'
        next_row = ''
        for j in range(len(c_row)-2):
            l,c,r = c_row[j:j+3]
            next_row += get_tile(l,c,r)
        rows.append(next_row)
    safe = 0
    for r in rows:
        safe += r.count('.')
    print 'The number of safe tiles is #1:',safe

if __name__ == '__main__':
    d18_1()
    d18_2()
