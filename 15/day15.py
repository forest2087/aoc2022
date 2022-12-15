import re
GRID_SZ = 9999999

def readInput(f, grid):
    sensors=[]
    beacons=[]
    while True:
        ln = f.readline()
    
        if not ln:
            break

        # print(list(map(int, re.findall(r'\d+', ln))))
        x1, y1, x2, y2 = list(map(int, re.findall(r'\d+', ln)))
        sensors.append((x1, y1))
        grid[x1][y1]='S'
        beacons.append((x2, y2))
        grid[x2][y2]='B'
    return (sensors, beacons)


def find_coordinates(x, y, distance):
    coordinates = []
    for i in range(-distance, distance+1):
        for j in range(-distance, distance+1):
            if abs(i) + abs(j) <= distance:
                coordinates.append((x+i, y+j))
    return coordinates

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def printGrid(grid):
    for i in range(-GRID_SZ//2, GRID_SZ//2):
        for j in range(-GRID_SZ//2, GRID_SZ//2):
            print(grid[i][j], end='')
        print('')
    

def solv1(f):
    
    grid = [['.']* GRID_SZ for _ in range(GRID_SZ)]
    sensors, beacons = readInput(f, grid)
    # d = manhattan_distance(sensors[0][0], sensors[0][1], beacons[0][0], beacons[0][1])
    # print(d)
    # print(sensors[0][0], sensors[0][1])
    # print(find_coordinates(sensors[0][0], sensors[0][1], d))

    for i in range(len(sensors)):
        d = manhattan_distance(sensors[i][0], sensors[i][1], beacons[i][0], beacons[i][1])
        for x,y in find_coordinates(sensors[i][0], sensors[i][1], d):
            if grid[x][y]=='.':
                grid[x][y]='#'
            
    # printGrid(grid)

    # print('')
    ret = 0
    for i in range(GRID_SZ):
        # print(grid[i][10], end='')
        if grid[i][10]=='#':
            ret+=1
    print(ret)
    

def solv2(f):
    a, b = readInput(f)