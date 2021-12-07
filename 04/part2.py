import sys
from bingo_board import BingoBoard

readings = sys.stdin.readlines()

numbers = [int(x) for x in readings[0].split(",")]

allBoards = []

idx = 1
while idx < len(readings):
    if readings[idx] == "\n":
        idx += 1
        continue
    allBoards.append(BingoBoard(readings[idx: idx+5]))
    idx += 5

winners = 0
N = len(allBoards)
for idx, number in enumerate(numbers):
    for board in allBoards:
        if board.completed:
            continue
        board.mark(number)
        if idx >= 4:
            if board.check():
                winners += 1
                board.completed = True
                if winners == N:
                    remaining = board.calcRemaining()
                    print(remaining * number)
                    break
    if winners == N:
        break
