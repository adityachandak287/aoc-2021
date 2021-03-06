import sys
from utils import parseLine

rawLines = sys.stdin.readlines()

lines = [parseLine(line) for line in rawLines]
straightLines = list(filter(lambda line: line.isStraightLine(), lines))

allPoints = set()
dangerPoints = set()
for line in straightLines:
    for point in line.traverse():
        if point in allPoints:
            dangerPoints.add(point)
        else:
            allPoints.add(point)

print(len(dangerPoints))
