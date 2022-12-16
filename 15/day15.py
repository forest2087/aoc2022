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
        x1, y1, x2, y2 = list(map(int, re.findall("(-?\d+)", ln)))
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


BOUND = 4000000


def solv2(f):
    sensors, beacons, offset = readInput(f)

    # print(beacons)
    # manhattan distance covers a diamond shaped area
    # if there is only one pt not covered, it should be on the line segment of the diamond just outside of the manhattan distance
    print(sensors)
    df = [1, 0, -1, 0, 1, 0]
    cnt = 1
    for x, y, d in sensors:
        print('checking sensor ', cnt)
        cnt+=1
        line = []
        for i in range(len(df) - 1):
            dx = x + d * df[i] + df[i]
            dy = y + d * df[i + 1] + df[i + 1]
            line.append((dx, dy))
        
        # print(line)
        gx = [-1, -1, 1, 1]
        gy = [-1, 1, 1, -1]
        for i in range(len(line) - 1):
            jx, jy = line[i]
            while jx != line[i + 1][0]:
                # print(jx, line[i + 1][0])
                if 0 < jx < BOUND and 0 < jy < BOUND and all(
                        manhattan_distance(jx, jy, sx, sy) > sd for sx, sy, sd in sensors):
                    print('FOUND IT', jx, jy)
                    print(4000000 * jx + jy)
                    return
                jx += gx[i]
                jy += gy[i]

