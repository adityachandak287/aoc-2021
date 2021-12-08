class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self):
        hash_value = hash(tuple((self.x, self.y)))
        return hash_value

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def display(self):
        print(f"({self.x},{self.y})")


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.p1 = point1
        self.p2 = point2

    def isStraightLine(self):
        return (self.p1.x == self.p2.x) ^ (self.p1.y == self.p2.y)

    def display(self):
        print(f"({self.p1.x},{self.p1.y}) -> ({self.p2.x}, {self.p2.y})")

    # Reference: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    def intersect(self, other):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        x3 = other.p1.x
        y3 = other.p1.y
        x4 = other.p2.x
        y4 = other.p2.y

        d = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if d == 0:
            return None
        x1y2_y1x2 = (x1 * y2 - y1 * x2)
        x3y4_y3x4 = (x3 * y4 - y3 * x4)
        px_n = x1y2_y1x2 * (x3-x4) - (x1-x2) * x3y4_y3x4
        py_n = x1y2_y1x2 * (y3-y4) - (y1-y2) * x3y4_y3x4
        return Point(px_n/d, py_n/d)

    def traverse(self):
        if self.p1.y == self.p2.y:
            lower = min(self.p1.x, self.p2.x)
            upper = max(self.p1.x, self.p2.x)
            for x in range(lower, upper+1):
                yield Point(x, self.p1.y)
        elif self.p1.x == self.p2.x:
            lower = min(self.p1.y, self.p2.y)
            upper = max(self.p1.y, self.p2.y)
            for y in range(lower, upper+1):
                yield Point(self.p1.x, y)
        else:
            xDir = 1 if self.p2.x > self.p1.x else -1
            yDir = 1 if self.p2.y > self.p1.y else -1
            x = self.p1.x
            y = self.p1.y
            for _ in range(abs(self.p2.x - self.p1.x) + 1):
                yield Point(x, y)
                x += xDir
                y += yDir


def parseLine(line):
    points = line.split(" -> ")
    [x1, y1] = [int(c) for c in points[0].split(",")]
    [x2, y2] = [int(c) for c in points[1].split(",")]
    return Line(Point(x1, y1), Point(x2, y2))
