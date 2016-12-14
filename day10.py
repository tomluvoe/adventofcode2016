import re

def value(data,state):
    chip,typ,num = re.findall('^([0-9]+?) .* (bot) ([0-9]+?)$',data)[0]
    bot = typ+'-'+num
    found = False
    for i,s in enumerate(state):
        if s['name'] == bot:
            state[i]['chips'].append(int(chip))
            state[i]['chips'].sort()
            found = True
    if not found:
        state.append({'name':bot,'chips':[int(chip)]})
    return state

def find_bots_with_two_chips(state):
    bots = []
    for i,s in enumerate(state):
        if len(s['chips']) >= 2:
            bots.append(i)
    return bots

def find_bot(name,state):
    for i,s in enumerate(state):
        if s['name'] == name:
            return i
    state.append({'name':name,'chips':[]})
    return len(state)-1

def execute_instruction(bot_pos,instructions,state):
    for [b,lo,hi] in instructions:
        if b == state[bot_pos]['name']:
            to_lo = find_bot(lo,state)
            to_hi = find_bot(hi,state)
            if 17 in state[bot_pos]['chips'] and 61 in state[bot_pos]['chips']:
                print 'Bot that compares microchips 17 and 61 is:',state[bot_pos]['name']
            state[to_lo]['chips'].append(state[bot_pos]['chips'][0])
            state[to_hi]['chips'].append(state[bot_pos]['chips'][1])
            state[to_lo]['chips'].sort()
            state[to_hi]['chips'].sort()
            state[bot_pos]['chips'] = []
    return state

def d10_1():
    state = []
    instr = []
    with open('day10.input','r') as file_data:
        for d in file_data:
            cmd,data = re.findall('(.+?) (.*)',d)[0]
            if cmd == 'bot':
                bot,lo0,lo1,hi0,hi1 = re.findall('^([0-9]+?) .* (bot|output) ([0-9]+?) .* (bot|output) ([0-9]+?)$',data)[0]
                instr.append(['bot-'+bot,lo0+'-'+lo1,hi0+'-'+hi1])
            elif cmd == 'value':
                state = value(data,state)
    bots_with_two_chips = find_bots_with_two_chips(state)
    while len(bots_with_two_chips) > 0:
        for b in bots_with_two_chips:
            state = execute_instruction(int(b),instr,state)
        bots_with_two_chips = find_bots_with_two_chips(state)
    #print state

if __name__ == "__main__":
    d10_1()
