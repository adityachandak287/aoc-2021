import sys
import statistics

positions = [int(x) for x in sys.stdin.readline().strip().split(",")]

median = statistics.median(positions)

fuel = sum([abs(pos - median) for pos in positions])

print(fuel)
