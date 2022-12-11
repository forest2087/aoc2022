def solv1(f):
    ret = 0
    while True:
        ln = f.readline().strip()
        if not ln: 
            break

        elf1, elf2 = ln.split(',')
        l, r = map(int, elf1.split('-'))
        # print(l, r)
        a = list(range(l, r+1))
        l, r = map(int, elf2.split('-'))
        # print(l, r)
        b = list(range(l, r+1))
        # print(a, b)
        c = set(a) & set(b)
        # print(c)
        if c==set(a) or c==set(b):
            ret+=1
    print(ret)
    return ret


def solv2(f):
    ret = 0
    while True:
        ln = f.readline().strip()
        if not ln: 
            break

        elf1, elf2 = ln.split(',')
        l, r = map(int, elf1.split('-'))
        # print(l, r)
        a = list(range(l, r+1))
        l, r = map(int, elf2.split('-'))
        # print(l, r)
        b = list(range(l, r+1))
        # print(a, b)
        c = set(a) & set(b)
        # print(c)
        if len(c):
            ret+=1
    print(ret)
    return ret



