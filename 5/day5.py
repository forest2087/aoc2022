def solv1(f):
    box=[[0]*10 for _ in range(10)]
    operations=[]
    # print(box)
    c = 0
    stack = True
    while True:
        ln = f.readline()

        if not ln:
            break

        if ln.strip()=='':
            stack = False
            ln=f.readline()
        # print(ln)
        #read 4 char at a time? 

        # read boxes
        if stack: 
            r = 0
            for i in range(0, len(ln), 4):
                t = ln[i:i+4].strip()
                # print(t, end='')
                if t:
                    t = t[1:2]
                box[c][r]=t
                r+=1
            # print()
            c+=1

        # read operations
        if not stack:
            item=ln.split()
            # print(item)
            operations.append(list(map(int, [item[1], item[3], item[5]])))

    
    # print(box)            
    # print(operations)

    stack = [] 
    # print('stack', stack)
    # move box into stack
    for i in range(len(box[0])):
        cur = [] 
        for j in range(len(box)):
            # print(j, i)
            # print(box[j][i])
            if box[j][i]!=0 and box[j][i]!='':
                cur.append(box[j][i])
        if len(cur):
            stack.append(cur[::-1])

    # print(stack)

    # move operations
    i = 0
    for op in operations:
        n, f, t = op
        # print(n, f, t)
        for _ in range(n):
            tmp = stack[f-1].pop()
            stack[t-1].append(tmp)
        # print('i:', i, 'stack:', stack)
        i+=1

    ret = []
    # get top stack
    for s in stack:
        ret.append(s[-1])
    print(''.join(ret))


    
def solv2(f):
    box=[[0]*10 for _ in range(10)]
    operations=[]
    # print(box)
    c = 0
    stack = True
    while True:
        ln = f.readline()

        if not ln:
            break

        if ln.strip()=='':
            stack = False
            ln=f.readline()
        # print(ln)
        #read 4 char at a time? 

        # read boxes
        if stack: 
            r = 0
            for i in range(0, len(ln), 4):
                t = ln[i:i+4].strip()
                # print(t, end='')
                if t:
                    t = t[1:2]
                box[c][r]=t
                r+=1
            # print()
            c+=1

        # read operations
        if not stack:
            item=ln.split()
            # print(item)
            operations.append(list(map(int, [item[1], item[3], item[5]])))

    
    # print(box)            
    # print(operations)

    stack = [] 
    # print('stack', stack)
    # move box into stack
    for i in range(len(box[0])):
        cur = [] 
        for j in range(len(box)):
            # print(j, i)
            # print(box[j][i])
            if box[j][i]!=0 and box[j][i]!='':
                cur.append(box[j][i])
        if len(cur):
            stack.append(cur[::-1])

    # print(stack)

    # move operations updated 
    # move 3 means 3item at a time
    i = 0
    for op in operations:
        n, f, t = op
        # print('-'*20)
        # print(n, f, t)
        # print('i:', i, 'before stack:', stack)
        f -=1
        t -=1
        tmp = stack[f][-n:] # last n elements
        del stack[f][len(stack[f]) - n:]# remove last n elemnts
        stack[t].extend(tmp)
        # print('i:', i, 'after stack:', stack)
        i+=1

    ret = []
    # get top stack
    for s in stack:
        ret.append(s[-1])
    print(''.join(ret))
    