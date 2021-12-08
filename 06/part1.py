import sys

state = [int(x) for x in sys.stdin.readline().strip().split(",")]

DAYS = 80

for _ in range(DAYS):
    dayCount = len(state)
    for idx, fish in enumerate(state):
        if fish > 0 and fish < 8:
            state[idx] -= 1
        elif fish == 8 and idx < dayCount:
            state[idx] -= 1
        elif fish == 0:
            state[idx] = 6
            state.append(8)

print(len(state))
