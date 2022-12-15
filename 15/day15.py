import re
TARGET = 2000000

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def readInput(f):
    sensors = []
    beacons = set()
    offset = 0
    while True:
        ln = f.readline()

        if not ln:
            break

        # print(list(map(int, re.findall(r'\d+', ln))))
        x1, y1, x2, y2 = list(map(int, re.findall(r'\d+', ln)))
        sensors.append((x1, y1, manhattan_distance(x1, y1, x2, y2)))
        if (x2, y2) not in beacons:
            beacons.add((x2, y2))
            if y2 == TARGET:
                offset += 1
    return (sensors, beacons, offset)


def find_coordinates(x, y, distance):
    coordinates = []
    for i in range(-distance, distance + 1):
        j = TARGET - y
        if abs(i) + abs(j) <= distance:
            coordinates.append(x + i)
    return coordinates


def solv1(f):
    sensors, beacons, offset = readInput(f)

    ret = []
    for i in range(len(sensors)):
        c = find_coordinates(sensors[i][0], sensors[i][1], sensors[i][2])
        print(i, len(c))
        ret.extend(c)

    print(len(set(ret)) - offset)


def solv2(f):
    a, b = readInput(f)
