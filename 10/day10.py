def solv1(f):
    x=1
    cycle = 1
    ans={}
    ans[1]=1
    while True:
        ln = f.readline().strip()
        
        if not ln:
            break

        
        if ln=='noop':
            cycle+=1
            ans[cycle]=x
        else:
            inc = int(ln.split()[1])
            cycle+=1
            ans[cycle]=x
            cycle+=1
            x+=inc
            ans[cycle]=x
    ret = 0
    k = [20, 60, 100, 140, 180, 220]
    for i in k:
        ret+=i*ans[i]
        # print(i)
    print(ret)


def updateCRT(x):
    CRT = '.'*(x-1) + '#'*3 + '.'*(40-x-2)
    return CRT
    
def solv2(f):
    x=1
    cycle = 1
    ans={}
    ans[1]=1
    CRT='###.....................................'
    ret='#'
    # print(updateCRT(10))
    # print(len(updateCRT(10)))
    while True:
        ln = f.readline().strip()
        
        if not ln:
            break

        
        if ln=='noop':
            cycle+=1
            ans[cycle]=x
            ret+=CRT[(cycle-1)%40]
            print(cycle, x, CRT, CRT[(cycle-1)%40])
        else:
            inc = int(ln.split()[1])
            cycle+=1
            ans[cycle]=x
            ret+=CRT[(cycle-1)%40]
            print(cycle, x, CRT, CRT[(cycle-1)%40])
            
            cycle+=1
            x+=inc
            ans[cycle]=x
            CRT=updateCRT(x)
            ret+=CRT[(cycle-1)%40]
            print(cycle, x, CRT, CRT[(cycle-1)%40])

        
    # ret = 0
    # k = [20, 60, 100, 140, 180, 220]
    # for i in k:
    #     ret+=i*ans[i]
        # print(i)
    j=0
    for i in ret:
        if j%40==39:
            print(i)
        else:
            print(i, end='')
        j+=1
    
    # print(ret)