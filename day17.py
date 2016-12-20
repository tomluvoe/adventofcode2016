import hashlib

data = 'pvhmgsws'
directions = ['U','D','L','R']
move = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
open_door = 'bcdef'

def valid_pos(x,y,d,path):
    x1 = x + move[d][0]
    y1 = y + move[d][1]
    if x1 > 0 and x1 < 4 and y1 > 0 and y1 < 4:
        h = hashlib.md5(data+path).hexdigest()

        return True
    return False

def d17_1():
    start = (0,3)
    goal = (3,0)
    search_list = [[0,'',start]]
    while len(search_list) > 0:
        dist,path,pos = search_list.pop(0)
        for d in directions:
            x,y = pos
            dx,dy = move[d]
            npath = path+d
            if valid_pos(x,y,path,npath):
                search_list.append([dist+1,npath,(x+dx,y+dy)])
                if x+dx == goal[0] and y+dy == goal[1]:
                    search_list = []
                    shortest_path =

if __name__ == '__main__':
    d17_1()
