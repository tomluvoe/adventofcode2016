def cpy(opt,state):
    #print 'cpy',opt
    if opt[0].isdigit() or opt[0][1:].isdigit():
        state[opt[1]] = int(opt[0])
    else:
        state[opt[1]] = state[opt[0]]
    return state

def jnz(opt,state):
    #print 'jnz',opt
    if opt[0].isdigit() and not opt[0] == '0':
        state['ptr'] += int(opt[1]) - 1
    if not opt[0].isdigit() and not state[opt[0]] == 0:
        state['ptr'] += int(opt[1]) - 1
    return state

def dec(opt,state):
    #print 'dec',opt
    state[opt[0]] -= 1
    return state

def inc(opt,state):
    #print 'inc',opt
    state[opt[0]] += 1
    return state

def run(program,state):
    while state['ptr'] < len(program):
        cmd = program[state['ptr']]
        if cmd[0] in ['cpy','inc','dec','jnz']:
            state = eval(cmd[0]+"(cmd[1:],state)")
        state['ptr'] += 1
    return state

if __name__ == '__main__':
    state = {'ptr':0, 'a':0, 'b':0, 'c':0, 'd':0}
    program = []
    with open('day12.input','r') as data:
        for d in data:
            program.append(d.split())
    state = run(program,state)
    print "Value of register a (init c=0) #1:",state['a']
    state = {'ptr':0, 'a':0, 'b':0, 'c':1, 'd':0}
    state = run(program,state)
    print "Value of register a (init c=1) #2:",state['a']
