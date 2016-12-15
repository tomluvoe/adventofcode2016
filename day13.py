def create_map(magic):
    size = 50
    maze = [[' ' for y in range(size)] for x in range(size)]
    for x in range(size):
        for y in range(size):
            val = x*x + 3*x + 2*x*y + y + y*y + magic
            if not bin(val).count('1') % 2 == 0:
                maze[x][y] = '#'
    return maze

def show_map(maze):
    print '------'
    for m in maze:
        for i in m:
            print i,
        print ''

move = [(1,0),(0,1),(-1,0),(0,-1)]

def search(start,goal,maze):
    search_list = []
    search_list.append([0,goal])
    not_found = True
    while not_found:
        pos = search_list.pop(0)
        if pos[1] == start:
            not_found = False
            continue
        for m in move:
            x,y = (pos[1][0]+m[0],pos[1][1]+m[1])
            if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
                continue
            if maze[x][y] == ' ':
                maze[x][y] = '*'
                search_list.append([pos[0]+1,[x,y]])
        search_list.sort()
#        show_map(maze)
    return pos

def count_positions(start,steps,maze):
    search_list = []
    search_list.append([0,start])
    not_found = True
    while not_found:
        pos = search_list.pop(0)
        if pos[0] >= steps:
            not_found = False
            continue
        for m in move:
            x,y = (pos[1][0]+m[0],pos[1][1]+m[1])
            if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
                continue
            if maze[x][y] == ' ':
                maze[x][y] = '*'
                search_list.append([pos[0]+1,[x,y]])
        search_list.sort()
    count = 0
    for x in maze:
        count += x.count('*')
#        show_map(maze)
    return count

def d13_1():
    magic = 1352
    maze = create_map(magic)
    goal = search([1,1],[31,39],maze)
    print 'The fewest number of steps to reach [31,39] is:',goal[0]

def d13_2():
    magic = 1352
    maze = create_map(magic)
    count = count_positions([1,1],50,maze)
    print 'The number of distinct positions possible to reach in 50 steps:',count

if __name__ == '__main__':
    d13_1()
    d13_2()
