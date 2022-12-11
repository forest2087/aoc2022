class Head:
    N=0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tx = x
        self.ty = y
        self.N = x*2
        self.visited=[[0]*self.N for _ in range(self.N)]
        self.visited[x][y] = 1
        self.cnt = 1

    def move(self, dir, step):
        if dir=='R':
            for _ in range(step):
                self.moveR()
        elif dir == 'L':
            for _ in range(step):
                self.moveL()
        elif dir == 'U':
            for _ in range(step):
                self.moveU()
        else:
            for _ in range(step):
                self.moveD()

    def moveU(self):
        if self.ty<self.y:
            self.ty+=1
            self.tx = self.x
            self.visited[self.tx][self.ty] = 1
        self.y+=1
        
    def moveD(self):
        if self.ty>self.y:
            self.ty-=1
            self.tx = self.x
            self.visited[self.tx][self.ty] = 1
        self.y-=1
        
    def moveL(self):
        if self.tx>self.x:
            self.tx-=1
            self.ty = self.y
            self.visited[self.tx][self.ty] = 1
        self.x-=1
        
    def moveR(self):
        if self.tx<self.x:
            self.tx+=1
            self.ty = self.y
            self.visited[self.tx][self.ty] = 1
        self.x+=1
    
    
    def get(self):
        return [self.x, self.y]

    def getTail(self):
        return [self.tx, self.ty]

    def getVisited(self):
        return self.visited
        
    def getCnt(self):
        return sum(map(sum, self.visited))
    

def solv1(f):
    visited = [[0]*10 for _ in range(10)]
    visited[0][0] = 1
    # print(visited)
    # print(sum(map(sum, visited)))

    h=Head(5000, 5000)
    # h.move('R', 4)
    
    while True:
        ln = f.readline().strip()
        if not ln:
            break
        dir,step = ln.split()
        print(dir, step)
        h.move(dir, int(step))

    print(h.get())
    print(h.getTail())
    # print(h.getVisited())
    print(h.getCnt())

class HeadTwo:
    N=0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tx = [x] * 9
        self.ty = [y] * 9
        self.N = x*2
        self.visited=[[0]*self.N for _ in range(self.N)]
        self.visited[x][y] = 1
        self.cnt = 1

    def move(self, dir, step):
        if dir=='R':
            for _ in range(step):
                self.moveR()
        elif dir == 'L':
            for _ in range(step):
                self.moveL()
        elif dir == 'U':
            for _ in range(step):
                self.moveU()
        else:
            for _ in range(step):
                self.moveD()

    def moveTail(self, x, y, i):
        tx = self.tx[i]
        ty = self.ty[i]
        # print(i, x, y, tx, ty)
        #move R
        if x-tx>1 and y==ty:
            tx+=1
        #move RU
        elif (x-tx>1 and y>ty) or (x>tx and y-ty>1):
            tx+=1
            ty+=1
        #move U
        elif x==tx and y-ty>1:
            ty+=1
        #move LU
        elif (tx-x>1 and y>ty) or (tx>x and y-ty>1) :
            tx-=1
            ty+=1
        #move L
        elif tx-x>1 and y==ty:
            tx-=1
        #move LD
        elif (tx-x> 1 and ty>y) or (tx>x and ty-y>1):
            tx-=1
            ty-=1
        #move D
        elif tx==x and ty-y>1:
            ty-=1
        #move RD
        elif (x-tx>1 and ty>y) or (x>tx and ty-y>1):
            tx+=1
            ty-=1

        self.tx[i] = tx
        self.ty[i] = ty
        
        
        # update visited for last knot
        if i==8:
            # print( self.tx, self.ty)
            self.visited[self.tx[i]][self.ty[i]] = 1
        else:
            self.moveTail(tx, ty, i+1)
    
    def moveU(self):
        self.y+=1
        self.moveTail(self.x, self.y, 0)
            
        
    def moveD(self):
        self.y-=1
        self.moveTail(self.x, self.y, 0)
        
    def moveL(self):
        self.x-=1
        self.moveTail(self.x, self.y, 0)
        
    def moveR(self):
        self.x+=1
        self.moveTail(self.x, self.y, 0)
    
    
    def get(self):
        return [self.x, self.y]

    def getTail(self):
        return [self.tx, self.ty]

    def getVisited(self):
        return self.visited
        
    def getCnt(self):
        return sum(map(sum, self.visited))
    
def solv2(f):

    h=HeadTwo(1000, 1000)
    
    while True:
        ln = f.readline().strip()
        if not ln:
            break
        dir,step = ln.split()
        # print(dir, step)
        h.move(dir, int(step))

    print(h.get())
    print(h.getTail())
    # print(h.getVisited())
    print(h.getCnt())