
def charToPriority(ch):
    # 97 a
    # 65 A
    ret = ord(ch)
    if ret>= 97:
        return ret-96
    else:
        return ret-64+26

def solv1(f):
    ret = 0
    while True:
        ln = f.readline()
        if not ln:
            break
        
        n = len(ln) // 2
        a = ln[:n]
        b = ln[n:]
        c = set(list(a)) & set(list(b))
        # print(a, b, ''.join(c).strip())
        c = ''.join(c)
        ret+=charToPriority(str(c)[0])
    f.close()
    print(ret)
    return ret

# solv('i')

def solv2(f):
    ret = 0
    i = 1
    cur=[]
    while True:
        ln = f.readline().strip()
        if not ln: 
            break;
        cur.append(ln)
        
        if i%3==0:
            a, b, c = cur
            # print(a, b, c)
            cur = []
            d = set(list(a)) & set(list(b)) & set(list(c))
            # print(d)
            ret+=charToPriority(''.join(d)[0])
        i+=1
    print(ret)
    return ret

# solv2('i')

