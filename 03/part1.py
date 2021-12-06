import sys

readings = sys.stdin.readlines()

gamma = 0
epsilon = 0

ans = [[0, 0] for _ in range(len(readings[0].strip()))]

for i, reading in enumerate(readings):
    for j, digit in enumerate(reading.strip()):
        ans[j][int(digit)] += 1

N = len(ans)
for index, [zero, one] in enumerate(ans):
    if zero > one:
        gamma += 0
        epsilon += 2**(N-(index+1))
    else:
        gamma += 2**(N-(index+1))
        epsilon += 0

print(gamma*epsilon)
