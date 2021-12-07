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

winner = False
for idx, number in enumerate(numbers):
    for board in allBoards:
        board.mark(number)
        if idx >= 4:
            if board.check():
                remaining = board.calcRemaining()
                print(number * remaining)
                winner = True
                break
    if winner:
        break
