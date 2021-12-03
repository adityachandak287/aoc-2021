import sys

moves = sys.stdin.readlines()

x = 0
y = 0
aim = 0

for move in moves:
    [action, unitString] = move.strip().split(" ")
    unit = int(unitString)
    if action == "forward":
        x += unit
        y -= aim * unit
    elif action == "up":
        aim -= unit
    elif action == "down":
        aim += unit

print(x * abs(y))
