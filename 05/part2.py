import sys
from utils import parseLine

rawLines = sys.stdin.readlines()

lines = [parseLine(line) for line in rawLines]

allPoints = set()
dangerPoints = set()
for line in lines:
    for point in line.traverse():
        if point in allPoints:
            dangerPoints.add(point)
        else:
            allPoints.add(point)

print(len(dangerPoints))
