import hashlib

data = 'pvhmgsws'
move = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
md5char = {'U':0,'D':1,'L':2,'R':3}
open_door = 'bcdef'

def valid_pos(x,y,d,path):
    x1 = x + move[d][0]
    y1 = y + move[d][1]
    if x1 >= 0 and x1 < 4 and y1 >= 0 and y1 < 4:
        h = hashlib.md5(data+path).hexdigest()
        if h[md5char[d]] in open_door:
            return True
    return False

def d17_2():
    start = (0,3)
    goal = (3,0)
    search_list = [[0,'',start]]
    longest_path = ''
    while len(search_list) > 0:
        dist,path,pos = search_list.pop(0)
        for d in move.keys():
            x,y = pos
            if valid_pos(x,y,d,path):
                npath = path+d
                dx,dy = move[d]
                search_list.append([dist+1,npath,(x+dx,y+dy)])
                if x+dx == goal[0] and y+dy == goal[1]:
                    search_list.pop(-1)
                    longest_path = dist+1
        search_list.sort()
    print 'The length of the longest path to reach the vault is:',longest_path

def d17_1():
    start = (0,3)
    goal = (3,0)
    search_list = [[0,'',start]]
    shortest_path = ''
    not_done = True
    while not_done:
        dist,path,pos = search_list.pop(0)
        for d in move.keys():
            x,y = pos
            if valid_pos(x,y,d,path):
                npath = path+d
                dx,dy = move[d]
                search_list.append([dist+1,npath,(x+dx,y+dy)])
                if x+dx == goal[0] and y+dy == goal[1]:
                    not_done = False
                    shortest_path = npath
        search_list.sort()
    print 'The shortest path to reach the vault is:',shortest_path

if __name__ == '__main__':
    d17_1()
    d17_2()
