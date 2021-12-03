import sys

moves = sys.stdin.readlines()

x = 0
y = 0

for move in moves:
    [action, unitString] = move.strip().split(" ")
    unit = int(unitString)
    if action == "forward":
        x += unit
    elif action == "up":
        y += unit
    elif action == "down":
        y -= unit

print(x * abs(y))
