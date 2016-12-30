import re
from itertools import permutations

def indexes(letter,string):
    return [p for p, c in enumerate(string) if c == letter]

def rotate_string(steps,string):
    steps = steps%len(string)
    if steps == 0:
        return string
    return string[-steps:]+string[:len(string)-steps]

def inv_rotate(passwd,instr):
    is_based_on = re.findall('based on position of letter (\w)',instr)
    if is_based_on:
        c = is_based_on[0]
        pos = passwd.index(c)
        steps = 0
        if pos == 0:
            passwd = rotate_string(-1,passwd)
        else:
            while pos != steps:
                pos = passwd.index(c)
                passwd = rotate_string(-1,passwd)
                steps += 1
                if steps == 5:
                    passwd = rotate_string(-1,passwd)
                steps = steps % len(passwd)
    else:
        a,b = re.findall('(\w+?) (\w+?) step',instr)[0]
        if a == 'left':
            passwd = rotate_string(int(b),passwd)
        else:
            passwd = rotate_string(-1*int(b),passwd)
    return passwd

def rotate(passwd,instr):
    is_based_on = re.findall('based on position of letter (\w)',instr)
    if is_based_on:
        c = is_based_on[0]
        steps = passwd.index(c)
        if steps >= 4:
            steps += 1
        steps += 1
        passwd = rotate_string(steps,passwd)
    else:
        a,b = re.findall('(\w+?) (\w+?) step',instr)[0]
        if a == 'left':
            passwd = rotate_string(-1*int(b),passwd)
        else:
            passwd = rotate_string(int(b),passwd)
    return passwd

def swap(passwd,instr):
    passwd = list(passwd)
    is_letters = re.findall('letter (\w) with letter (\w)',instr)
    if is_letters:
        a,b = is_letters[0]
        c = indexes(a,passwd)
        d = indexes(b,passwd)
        for i in c:
            passwd[i] = b
        for i in d:
            passwd[i] = a
    else:
        a,b = re.findall('position (\w) with position (\w)',instr)[0]
        tmp = passwd[int(a)]
        passwd[int(a)] = passwd[int(b)]
        passwd[int(b)] = tmp
    return ''.join(passwd)

def reverse(passwd,instr):
    a,b = re.findall('positions (\w) through (\w)',instr)[0]
    p0 = passwd[:int(a)]
    p1 = passwd[int(a):int(b)+1][::-1]
    p2 = passwd[int(b)+1:]
    return p0+p1+p2

def move(passwd,instr):
    passwd = list(passwd)
    a,b = re.findall('position (\w) to position (\w)',instr)[0]
    c = passwd.pop(int(a))
    passwd.insert(int(b),c)
    return ''.join(passwd)

def inv_move(passwd,instr):
    passwd = list(passwd)
    a,b = re.findall('position (\w) to position (\w)',instr)[0]
    c = passwd.pop(int(b))
    passwd.insert(int(a),c)
    return ''.join(passwd)

def d21_1():
    operations = []
    output = []
    start = 'abcdefgh'
    passwd = start
    with open('day21.input','r') as data:
        for d in data:
            operations.append(re.findall('(\w+?) (.*)',d)[0])
    for o in operations:
        if o[0] in ['rotate','swap','reverse','move']:
            passwd = eval(o[0]+'(passwd,o[1])')
            output.append(passwd)
    print 'The result of scrambling the password is #1:',passwd
    return operations,start,output

def brute(operations,scrambled):
    guess = [''.join(p) for p in permutations('abcdefgh')]
    for g in guess:
        passwd = g
        for o in operations:
            if o[0] in ['rotate','swap','reverse','move']:
                passwd = eval(o[0]+'(passwd,o[1])')
        if scrambled == passwd:
            return g
    return ''

def d21_2():
    operations = []
#    passwd = 'fbgdceah'
    with open('day21.input','r') as data:
        for d in data:
            #operations.insert(0,re.findall('(\w+?) (.*)',d)[0])
            operations.append(re.findall('(\w+?) (.*)',d)[0])
#    operations = [[o[0],o[1]] for o in operations]
#    for i,o in enumerate(operations):
#        if o[0] in ['rotate','move']:
#            operations[i][0] = 'inv_'+o[0]
#    for o in operations:
#        if o[0] in ['rotate','swap','reverse','move','inv_rotate','inv_move']:
#            passwd = eval(o[0]+'(passwd,o[1])')
#    print 'The result of un-scrambled password is #2:',passwd
    print 'The result of un-scrambled password is #2 (brute force):',brute(operations,'fbgdceah')

def test_operations(operations,start,output):
    passwd = start
    for i,o in enumerate(operations):
        if o[0] in ['rotate','swap','reverse','move','inv_rotate','inv_move']:
            passwd = eval(o[0]+'(passwd,o[1])')
            assert passwd == output[i]

def invert_test_data(operations,start,output):
    operations = operations[::-1]
    output.insert(0,start)
    start = output.pop()
    output = output[::-1]
    for i,o in enumerate(operations):
        if o[0] in ['rotate','move']:
            operations[i][0] = 'inv_'+o[0]
    return operations,start,output

def d21_test():
    operations = []
    operations.append(['swap','position 4 with position 0'])
    operations.append(['swap','letter d with letter b'])
    operations.append(['reverse','positions 0 through 4'])
    operations.append(['rotate','left 1 step'])
    operations.append(['move','position 1 to position 4'])
    operations.append(['move','position 3 to position 0'])
    operations.append(['rotate','based on position of letter b'])
    operations.append(['rotate','based on position of letter d'])
    output = []
    start = 'abcde'
    output.append('ebcda')
    output.append('edcba')
    output.append('abcde')
    output.append('bcdea')
    output.append('bdeac')
    output.append('abdec')
    output.append('ecabd')
    output.append('decab')
    print 'Running test #1..'
    test_operations(operations,start,output)
    print 'OK'
    operations,start,output = invert_test_data(operations,start,output)
    print 'Running test #2..'
    test_operations(operations,start,output)
    print 'OK'

def d21_test_2(op,st,out):
    print 'Running test #3..'
    test_operations(op,st,out)
    print 'OK'
    op = [[o[0],o[1]] for o in op]
    op,st,out = invert_test_data(op,st,out)
    print 'Running test #4..'
    test_operations(op,st,out)
    print 'OK'

if __name__ == '__main__':
#    d21_test() # test examples, scramble and un-scramble
    op,st,out = d21_1()
#    d21_test_2(op,st,out) # test part 1, scramble and un-scramble
    d21_2()
