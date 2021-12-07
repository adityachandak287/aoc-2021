class BingoBoard:
    def __init__(self, rows):
        self.rows = 5
        self.cols = 5
        self.board = []
        self.all = set()
        for row in rows:
            currRow = [int(x) for x in row.strip().split()]
            self.board.append(currRow)
            self.all.update(currRow)

    def display(self):
        for row in self.board:
            print(row)

    def mark(self, number):
        if number in self.all:
            for row in self.board:
                for idx, col in enumerate(row):
                    if col == number:
                        row[idx] = -1
                        break

    def check(self):
        colFlags = [True] * self.cols
        for row in self.board:
            rowFlag = True
            for idx, col in enumerate(row):
                if col != -1:
                    rowFlag = False
                    colFlags[idx] = False
            if rowFlag == True:
                return True
        return any(colFlags)

    def calcRemaining(self):
        remaining = 0
        for row in self.board:
            for col in row:
                if col != -1:
                    remaining += col
        return remaining
