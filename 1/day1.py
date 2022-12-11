def solv1(f):
    most = 0
    curr = 0
    while True:
        ln = f.readline()
        # print(ln)

        if not ln:
            most = max(most, curr)
            break

        if ln=='\n':
            most = max(most, curr)
            curr = 0
        else:
            curr+=int(ln)
    print(most)
    
import heapq
def solv2(f):
    elfs = []
    curr = 0
    while True:
        ln = f.readline()
        # print(ln)

        if not ln:
            # print(curr)
            elfs.append(curr)
            break

        if ln=='\n':
            # print(curr)
            elfs.append(curr)
            curr = 0
        else:
            curr+=int(ln)
    print(sum(heapq.nlargest(3, elfs)))
    print(sum(sorted(elfs, reverse=True)[:3]))
    