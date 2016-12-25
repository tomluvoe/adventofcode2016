import re

def indexes(letter,string):
    return [p for p, c in enumerate(string) if c == letter]

def rotate_string(steps,string):
    steps = steps%len(string)
    if steps == 0:
        return string
    return string[-steps:]+string[:len(string)-steps]

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

def d21_1():
    operations = []
    passwd = 'abcdefgh'
    with open('day21.input','r') as data:
        for d in data:
            operations.append(re.findall('(\w+?) (.*)',d)[0])
    for o in operations:
        if o[0] in ['rotate','swap','reverse','move']:
            passwd = eval(o[0]+'(passwd,o[1])')
    print 'The result of scrambling the password is:',passwd

def d21_test():
    passwd = 'abcde'
    passwd = swap(passwd,'position 4 with position 0')
    assert passwd == 'ebcda'
    passwd = swap(passwd,'letter d with letter b')
    assert passwd == 'edcba'
    passwd = reverse(passwd,'reverse positions 0 through 4')
    assert passwd == 'abcde'
    passwd = rotate(passwd,'left 1 step')
    assert passwd == 'bcdea'
    passwd = move(passwd,'position 1 to position 4')
    assert passwd == 'bdeac'
    passwd = move(passwd,'position 3 to position 0')
    assert passwd == 'abdec'
    passwd = rotate(passwd,'based on position of letter b')
    assert passwd == 'ecabd'
    passwd = rotate(passwd,'based on position of letter d')
    assert passwd == 'decab'
    return True

if __name__ == '__main__':
    if d21_test():
        print 'Unit test OK'
    d21_1()
