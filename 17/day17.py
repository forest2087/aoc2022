def readInput(f):
    jet = []
    while True:
        ln = f.readline()
    
        if not ln:
            break

        jet.extend([1 if x=='>' else -1 for x in ln])
    return jet
    

def solv1(f):
    jet = readInput(f)
    print(jet)

def solv2(f):
    a, b = readInput(f)