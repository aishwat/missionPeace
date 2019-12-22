class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"


def solveNQueenUtil(N, row, positions):
    if row == N:
        # print("--------roe ==n")
        return True

    for col in range(N):
        # print('checking', row, col)
        foundSafe = checkISSafe(row, col, positions)

        if foundSafe:
            positions.append(Position(row, col))
            # add point to positions
            print(positions)
            if solveNQueenUtil(N, row + 1, positions):
                return True
            else:
                # try next column, when out of rec
                continue

    print("--------out of for")
    # pop from positions
    positions.pop()
    return False


def checkISSafe(row, col, positions):
    for pos in positions:
        # print(row, col, positions)
        # print(pos.col == col, pos.row == row, (pos.row - pos.col) == (row - col), (pos.row + pos.col) == (row + col))
        # print()
        if pos.col == col or pos.row == row or (pos.row - pos.col) == (row - col) or (pos.row + pos.col) == (row + col):
            return False
    return True


def solveNQueen():
    # hasSol = solveNQueenUtil(4, 0, [])
    hasSol = solveNQueenUtil(4, 0, [])
    print(hasSol)


solveNQueen()

# If just need one solution, there's a direct formula O(1)
# wiki = https://en.wikipedia.org/wiki/Eight_queens_puzzle (existence of solution)
#
# If the remainder from dividing n by 6 is not 2 or 3 then the list is simply all even numbers followed by all odd numbers not greater than n.
# Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).
# If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).
# If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 1, 3).
# Append odd list to the even list and place queens in the rows given by these numbers, from left to right (a2, b4, c6, d8, e3, f1, g7, h5).
