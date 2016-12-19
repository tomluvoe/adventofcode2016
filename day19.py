class Elf:
    def __init__(self,elf):
        self.elf = elf
        self.next = None
        self.prev = None
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

def d19_2():
    data = 3018458
    elfs = map(Elf,xrange(data))
    for i in range(data):
        elfs[i].next = elfs[(i+1)%data]
        elfs[i].prev = elfs[(i-1)%data]
    pos = elfs[0]
    mid = elfs[data/2]
    for i in range(data-1):
        mid.remove()
        mid = mid.next
        if (data-i) % 2 == 1:
            mid = mid.next
        pos = pos.next
    print 'The elf that gets all the presents is #2:',pos.elf+1

def white_elefant_round(data):
    return [x for i,x in enumerate(data) if i%2 == 0]

def d19_1():
    data = 3018458
    elfs = range(data)
    while len(elfs) > 1:
        if len(elfs) % 2 == 0:
            elfs = white_elefant_round(elfs)
        else:
            elf = elfs.pop()
            elfs = white_elefant_round(elfs)
            elfs.insert(0,elf)
    print 'The elf that gets all the presents is #1:',elfs[0]+1

if __name__ == '__main__':
    d19_1()
    d19_2()
