import functools

def readInput(f):
    a=[]
    b=[]
    while True:
        ln = f.readline()
    
        if not ln:
            break

        if ln.strip()=='':
            continue
        
        tmp = eval(ln.strip())
        a.append(tmp)
        tmp = eval(f.readline().strip())
        b.append(tmp)

    return (a, b)
            
def spaceOperator(a, b):
    if a==b:
        return 0
    elif a<b:
        return -1
    else:
        return 1

def comp(a, b):
    # print('comparing', a, b)
    
    if type(a) is int and type(b) is int: 
        return spaceOperator(a, b)

    if type(a) is int:
        a = [a]
    if type(b) is int:
        b = [b]

    for i,v in enumerate(a):
        if i==len(b):
            return 1
        tmp = comp(v, b[i])
        if tmp!=0:
            return tmp

    return spaceOperator(len(a), len(b))
    

def solv1(f):
    a, b = readInput(f)
    ret = []
    for i in range(len(a)):
        if comp(a[i], b[i])==-1:
            ret.append(i+1)
    # print(ret)
    print(sum(ret))

def solv2(f):
    a, b = readInput(f)
    c = a + b + [[2], [6]]
    d = sorted(c, key=functools.cmp_to_key(comp))
    # print(d)
    print((d.index([2])+1)*(d.index([6])+1))
