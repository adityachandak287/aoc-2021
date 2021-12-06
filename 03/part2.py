import sys

readings = sys.stdin.readlines()

rows = len(readings)
cols = len(readings[0].strip())

validOxygenRows = set(range(rows))
validCo2Rows = set(range(rows))
ansOxygen = [[0, 0] for _ in range(cols)]
ansCo2 = [[0, 0] for _ in range(cols)]

for j in range(cols):
    for i in range(rows):
        digit = int(readings[i][j])
        if i in validOxygenRows:
            ansOxygen[j][digit] += 1
        if i in validCo2Rows:
            ansCo2[j][digit] += 1

    for i in range(rows):
        digit = int(readings[i][j])
        mostCommon = 1 if ansOxygen[j][1] >= ansOxygen[j][0] else 0
        leastCommon = 0 if ansCo2[j][0] <= ansCo2[j][1] else 1

        if digit != mostCommon and len(validOxygenRows) > 1:
            validOxygenRows.discard(i)
        if digit != leastCommon and len(validCo2Rows) > 1:
            validCo2Rows.discard(i)

    if len(validOxygenRows) == 1 and len(validCo2Rows) == 1:
        break

oxygenRating = int(readings[validOxygenRows.pop()], 2)
co2Rating = int(readings[validCo2Rows.pop()], 2)

print(oxygenRating * co2Rating)
