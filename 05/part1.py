import sys
from utils import Point, Line

rawLines = sys.stdin.readlines()


def parseLine(line):
    points = line.split(" -> ")
    [x1, y1] = [int(c) for c in points[0].split(",")]
    [x2, y2] = [int(c) for c in points[1].split(",")]
    return Line(Point(x1, y1), Point(x2, y2))


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
