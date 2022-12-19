import re
def readInput(f):
    valve_rate={}
    valve_lead={}
    i = 0
    while True:
        ln = f.readline()
        
        if not ln:
            break

        # print(int(re.search("(-?\d+)", ln)[0]))
        flow = int(re.search("(-?\d+)", ln)[0])
        # print([ord(x[0]) - 65 for x in re.findall("[A-J]{2}", ln)[1:]])
        parts = re.findall("[A-Z]{2}", ln)
        
        valve_rate[parts[0]] = flow
        if flow>0:
            i+=1
        valve_lead[parts[0]] = parts[1:]
    print(i)
    return (valve_rate, valve_lead)
        
def solv1(f):
    a, b = readInput(f)
    print(a)
    print(b)

def solv2(f):
    a, b = readInput(f)