def solv1(f):
    while True:
        ln=f.readline()
        if not ln: 
            return
        for i in range(len(ln)):
            l = ln[i:i+4]
            # print(l)
            if len(set(l))==4:
                print(i+4)
                break
        
    return

def solv2(f):
    while True:
        ln=f.readline()
        if not ln: 
            return
        for i in range(len(ln)):
            l = ln[i:i+14]
            # print(l)
            if len(set(l))==14:
                print(i+14)
                break
        
    return