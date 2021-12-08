import sys

stateMap = {x: 0 for x in range(9)}

for x in sys.stdin.readline().strip().split(","):
    stateMap[int(x)] += 1

DAYS = 256

for _ in range(DAYS):
    temp = {x: 0 for x in range(9)}
    for fishState in stateMap:
        if fishState > 0:
            temp[fishState - 1] += stateMap[fishState]
        elif fishState == 0:
            temp[6] += stateMap[fishState]
            temp[8] += stateMap[fishState]
    stateMap.clear()
    stateMap.update(temp)

print(sum(stateMap.values()))
