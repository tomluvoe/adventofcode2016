import hashlib
import re

# from multiprocessing import Pool
# def get_hash(indata):
#     [salt,stretch] = indata
#     h = hashlib.md5(salt).hexdigest()
#     for i in range(stretch):
#         h = hashlib.md5(h).hexdigest()
#     return h
# def pool_hashes(salt,index,stretch):
#     p = Pool(processes=4)
#     args = []
#     for i in range(index):
#         args.append([salt+str(i),stretch])
#     hashes = p.map(get_hash,args)
#     return hashes

def d14(salt,stretch=0):
    idx = 0
    hashes = []
    keys = []
    not_done = True
    queue = 1000
#    hashes = pool_hashes(salt,queue-1,stretch)
    while not_done:
        hashes.append(hashlib.md5(salt+str(idx)).hexdigest())
        for i in range(stretch):
            hashes[-1] = hashlib.md5(hashes[-1]).hexdigest()
        if len(hashes) == queue:
            hash0 = hashes.pop(0)
            matches = re.findall(r"(\w)\1{2,}",hash0)
            if len(matches) > 0:
                found = False
                for i,h in enumerate(hashes):
                    k = re.findall(matches[0]*5,h)
                    if len(k) > 0:
                        keys.append(hash0)
                        found = True
                        if len(keys) > 63:
                            not_done = False
                            break
                    if found:
                        break
        if not_done:
            idx += 1
    print "The index that produces the 64th key is ("+str(stretch)+"):",idx-queue+1

if __name__ == '__main__':
    salt = 'jlmsuwbz'
    d14(salt)
    d14(salt,2016)
