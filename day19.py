def white_elefant(data):
    return [x for i,x in enumerate(data) if i%2 == 0]

def d19_1():
    data = 3018458
    elfs = range(data)
    while len(elfs) > 1:
        if len(elfs) % 2 == 0:
            elfs = white_elefant(elfs)
        else:
            elf = elfs.pop()
            elfs = white_elefant(elfs)
            elfs.insert(0,elf)
    print 'The elf that gets all the presents is:',elfs[0]+1

if __name__ == '__main__':
    d19_1()
