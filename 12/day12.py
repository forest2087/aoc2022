import queue

def readInput(f):
    grid=[]
    while True:
        ln = f.readline().strip()
    
        if not ln:
            break
        grid.append([ord(x)-97 for x in ln.split()[0]])
        
    return grid


START = -14
END = -28
def checkCord(dx, dy, s, grid, curNum):
    R = len(grid)
    C = len(grid[0])

    if dx<0 or dx>=R or dy<0 or dy>=C:
        return False
    
    destination = grid[dx][dy]
    if destination==START:
        destination = 0
    if destination==END:
        destination = 26
        
    if destination-curNum>1  or (dx, dy) in s:
        return False
    return True
    
def solv1(f):

    #-14 = start
    #-28 = end

    grid = readInput(f)
    # print(grid)
    
    q = queue.Queue()
    s = set()

    #get starting pos
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==START:
                q.put((i,j))
                s.add((i, j))
                break                

    step = 0
    offset = [1, 0, -1, 0, 1]
    while (not q.empty()):
        sz = q.qsize()

        for i in range(sz):
            x, y = q.get()
            
            # print('checking ', x, y, grid[x][y])
            if grid[x][y]==END:
                print('total steps:', step)
                return step

            curNum = grid[x][y]
            if curNum==START:
                curNum = 0
                
            # visit the neighbors
            for j in range(len(offset)-1):
                dx = x + offset[j]
                dy = y + offset[j+1]
                # print('next ', dx, dy)
                # print(checkCord(dx, dy, s, grid, curNum))
                if checkCord(dx, dy, s, grid, curNum):
                    q.put((dx, dy))
                    s.add((dx, dy))

        step+=1

    # print(step)

    
def checkCordTwo(dx, dy, s, grid, curNum):
    R = len(grid)
    C = len(grid[0])

    if dx<0 or dx>=R or dy<0 or dy>=C:
        return False


    destination = grid[dx][dy]
    if destination==START:
        destination = 0
    if destination==END:
        destination = 25
        
    if curNum-destination>1  or (dx, dy) in s:
        return False
    return True
      
    

def solv2(f):
    # from z to a, shortest, reverse the logic
    #-14 = start
    #-28 = end

    grid = readInput(f)
    # print(grid)
    
    q = queue.Queue()
    s = set()

    START_CORD = ()
    END_CORD = ()
    #get starting pos
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==START:
                START_CORD = (i,j)
            if grid[i][j]==END:
                q.put((i,j))
                s.add((i, j))
                END_CORD = (i, j)
                

    step = 0
    offset = [1, 0, -1, 0, 1]
    while (not q.empty()):
        sz = q.qsize()

        for i in range(sz):
            x, y = q.get()
            
            # print('checking ', x, y, grid[x][y])
            if grid[x][y]==0 or grid[x][y]==START:
                print('total steps:', step)
                return step

            curNum = grid[x][y]
            if curNum==END:
                curNum = 25
                
            # visit the neighbors
            for j in range(len(offset)-1):
                dx = x + offset[j]
                dy = y + offset[j+1]
                # print('next ', dx, dy)
                # print(checkCord(dx, dy, s, grid, curNum))
                if checkCordTwo(dx, dy, s, grid, curNum):
                    q.put((dx, dy))
                    s.add((dx, dy))

        step+=1

    # print(step)