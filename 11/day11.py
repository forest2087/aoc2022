import math

def evalOp(old, op):
    op=op.split('=')[1]
    return eval(op)
    
def solv1(f):
    items=[] #money items
    op=[] #operation
    div=[] #divisible
    tm = [] #true
    fm = [] #false
    j = 0
    while True:
        ln = f.readline()
            
        if not ln:
            break

        if ln.strip()=='':
            j+=1
            continue

        parts=ln.strip().split(':')

        if 'Starting' in parts[0]:
            items.append(list(map(int, parts[1].split(','))))
            # print(items)

        if 'Operation' in parts[0]:
            op.append(parts[1])

        if 'Test' in parts[0]:
            div.append(int(parts[1].split()[2]))

        if 'true' in parts[0]:
            tm.append(int(parts[1].split()[3]))

        if 'false' in parts[0]:
            fm.append(int(parts[1].split()[3]))

    # print(items)
    # print(op)
    # print(div)
    # print(tm)
    # print(fm)
    print(j) #0 indexed, tot j+1 monkeys

    cnt=[0]*(j+1) #keep money items per round
    # print('cnt', cnt)
    #start round
    for _ in range(20): #20 rounds
            
        for i in range(j+1): #iter each monkey
            for item in items[i]:
                cnt[i]+=1 #inc cnt
                new = evalOp(item, op[i])
                new = new // 3
                if new%div[i]==0:
                    items[tm[i]].append(new)
                else:
                    items[fm[i]].append(new)
            items[i]=[] # remove items from cur monkey after 1 round, all items thrown to another monkey
        # print(items)
        

    # print(items)
    # print(cnt)
    cnt.sort(reverse=True)
    print(cnt)
    print(cnt[0]*cnt[1])

# for python version < 3.9    
def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd (a, b)
    return a
    
def solv2(f):
    items=[] #money items
    op=[] #operation
    div=[] #divisible
    tm = [] #true
    fm = [] #false
    j = 0
    while True:
        ln = f.readline()
            
        if not ln:
            break

        if ln.strip()=='':
            j+=1
            continue

        parts=ln.strip().split(':')

        if 'Starting' in parts[0]:
            items.append(list(map(int, parts[1].split(','))))
            # print(items)

        if 'Operation' in parts[0]:
            op.append(parts[1])

        if 'Test' in parts[0]:
            div.append(int(parts[1].split()[2]))

        if 'true' in parts[0]:
            tm.append(int(parts[1].split()[3]))

        if 'false' in parts[0]:
            fm.append(int(parts[1].split()[3]))

    # print(items)
    # print(op)
    # print(div)
    # print(tm)
    # print(fm)
    print(j) #0 indexed, tot j+1 monkeys
    mlcm = lcm(*div)
    print(mlcm)
    # return

    cnt=[0]*(j+1) #keep money items per round
    # print('cnt', cnt)
    #start round
    for _ in range(10000): #10000 rounds
        # print(k, cnt)    
        for i in range(j+1): #iter each monkey
            for item in items[i]:
                cnt[i]+=1 #inc cnt
                new = evalOp(item, op[i])
                new = new%mlcm
                if new%div[i]==0:
                    items[tm[i]].append(new)
                else:
                    items[fm[i]].append(new)
            items[i]=[] # remove items from cur monkey after 1 round, all items thrown to another monkey
        # print(items)
        

    # print(items)
    # print(cnt)
    cnt.sort(reverse=True)
    print(cnt)
    print(cnt[0]*cnt[1])
            