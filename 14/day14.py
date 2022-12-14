def naiveDrawLine(x1, y1, x2, y2, grid, limits):
    def updateLimit(limits, x, y):
        if x>limits['right']:
            limits['right'] = x
        if x<limits['left']:
            limits['left'] = x
        if y>limits['bottom']:
            limits['bottom'] = y
        return limits
    if x1>x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    for x in range(x1, x2 + 1):
        if y1<y2:
            for y in range(y1, y2+1):
                # print(x, y)
                limits = updateLimit(limits, x, y)
                grid[x][y] = '#'
        else:
            for y in range(y2, y1+1):
                # print(x, y)
                limits = updateLimit(limits, x, y)
                grid[x][y] = '#'
    # print(grid)
    return (limits, grid)

def processPts(pts, grid, limits):
    for i in range(len(pts)-1):
        limits, grid = naiveDrawLine(int(pts[i][0]), int(pts[i][1]), int(pts[i+1][0]), int(pts[i+1][1]), grid, limits)
    return (limits, grid)

def printGrid(grid, limits):
    grid[500][0] = 'o'
    for j in range(limits['bottom']+2):
        for i in range(limits['left']-20, limits['right']+20):
            print(grid[i][j], end='')
        print('')

GRID_SZ=1100
def readInput(f):
    limits = {
        'left':999, 
        'right':0,
        'bottom':0
    }
    grid = [['.'] * GRID_SZ for _ in range(GRID_SZ)]
    while True:
        ln = f.readline()
        
        if not ln:
            break

        pts = ln.strip().split('->')
        pts = [x.split(',') for x in pts]
        limits, grid = processPts(pts, grid, limits)

    # printGrid(grid, limits)
    # print(limits)
    return (grid, limits)


def withinRange(limits, x, y):
    if x<limits['left']:
        return False
    if x>limits['right']:
        return False
    if y>limits['bottom']:
        return False
    return True

def withinRangeTwo(limits, y):
    if limits['bottom']-y==1:
        return False
    return True
    
def dropTwo(grid, limits, x, y):
    while grid[x][y+1]=='.':
        y+=1
    if limits['bottom']-y==1:
        # print(f"sand lands {x}, {y}")
        grid[x][y] = 'o'
        return (x, y)
    #try down left
    if grid[x-1][y+1]=='.' :
        return dropTwo(grid, limits, x-1, y+1)
        
    #try down right
    if grid[x+1][y+1]=='.':
        return dropTwo(grid, limits, x+1, y+1)

    # print(f"sand lands {x}, {y}")
    grid[x][y] = 'o'
    # printGrid(grid, limits)
    # if x==500 and y==0:
    #     return (-1, -1)
    return (x, y)
    
def drop(grid, limits, x, y, two=False):
    if two:
        return dropTwo(grid, limits, x, y)
    # print('drop from: ', x, y)
    while withinRange(limits, x, y+1) and grid[x][y+1]=='.' :
        y+=1
        # print('sand here: ', x, y)
    
    if not withinRange(limits, x, y):
        return (-1, -1)

    #try down left
    if grid[x-1][y+1]=='.' :
        return drop(grid, limits, x-1, y+1)
        
    
    #try down right
    if grid[x+1][y+1]=='.':
        return drop(grid, limits, x+1, y+1)

    #sand stay at x, y
    #update grid
    # print(f"sand lands {x}, {y}")
    grid[x][y] = 'o'
    # printGrid(grid, limits)
    if x==500 and y==0:
        return (-1, -1)
    return (x, y)
    
    

# sand starts at 500, 0
def dropSand(grid, limits, two=False):
    #return (-1, -1) if outside of limits
    #otherwise return where sand settles (x, y)
    x = 500
    y = 0
    ret = 0
    i, j = drop(grid, limits, x, y, two)
    
    while i!=-1 and not (i==500 and j==0):
        i, j = drop(grid, limits, x, y, two)
        ret+=1
        # print(ret, i, j)
    if i==500 and j==0:
        ret+=1
    return ret

def solv1(f):
    grid, limits=readInput(f)
    ret = dropSand(grid, limits)
    printGrid(grid, limits)
    print(ret)
    

def solv2(f):
    grid, limits=readInput(f)
    limits['bottom']+=2
    for i in range(GRID_SZ):
        grid[i][limits['bottom']] = '#'
    ret = dropSand(grid, limits, True)
    printGrid(grid, limits)
    print(ret)