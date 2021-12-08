import sys
import math

positions = [int(x) for x in sys.stdin.readline().strip().split(",")]

mean = sum(positions) / len(positions)
mUpper = math.ceil(mean)
mLower = math.floor(mean)

cost = {mUpper: 0, mLower: 0}
for pos in positions:
    for m in [mUpper, mLower]:
        diff = abs(pos - m)
        cost[m] += (diff * (diff + 1)) / 2

print(min(cost.values()))
