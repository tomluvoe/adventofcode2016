class IP:
    def __init__(self,low,high):
        self.low = low
        self.high = high
        self.next = None
        self.prev = None

    def remove(self):
        self.high = '-'
        self.low = '-'

    def blacklist(self,low,high):
        if low > self.high or high < self.low:
            return
        if low > self.low:
            if high >= self.high:
                self.high = low-1
            else:
                new = IP(high+1,self.high)
                self.high = low-1
                new.next = self.next
                new.prev = self
                self.next = new
        else:
            if high >= self.high:
                self.remove()
            else:
                self.low = high+1

def d20_2():
    ips = IP(0,4294967295)
    blacklist = []
    with open('day20.input','r') as data:
        for d in data:
            blacklist.append(d.rsplit()[0])
    for b in blacklist:
        ip = ips
        while ip:
            blk = b.split('-')
            ip.blacklist(int(blk[0]),int(blk[1]))
            ip = ip.next
    ip = ips
    allowed_ips = 0
    while ip:
        if ip.low != '-':
            allowed_ips += ip.high-ip.low+1
        ip = ip.next
    print 'The number of IPs that are allowed by the blacklist is:',allowed_ips

def d20_1():
    ips = IP(0,4294967295)
    blacklist = []
    with open('day20.input','r') as data:
        for d in data:
            blacklist.append(d.rsplit()[0])
    for b in blacklist:
        ip = ips
        while ip:
            blk = b.split('-')
            ip.blacklist(int(blk[0]),int(blk[1]))
            ip = ip.next
    ip = ips
    while ip:
        if ip.low != '-':
            first_ip = ip.low
            break
        ip = ip.next
    print 'The lowest-valued IP that is not blocked is:',first_ip

if __name__ == '__main__':
    d20_1()
    d20_2()
