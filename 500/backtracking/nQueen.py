# //practice


def isSafe(N, row, col, positions):
    for (r, c) in positions:
        if r == row or c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def getPositions(N, row, positions):
    if row == N:
        print("DONE")
        print(positions)
        return True

    for col in range(N):
        _isSafe = isSafe(N, row, col, positions)
        print("trying", row, " ", col, " ", _isSafe)

        if _isSafe:
            positions.append((row, col))
            print(positions)
            if getPositions(N, row + 1, positions):
                return True
            else:
                # try next col
                continue
    # if out of this loop, means all cols tried for this row, pop out
    print("popping",positions[-1] )
    positions.pop()
    return False


# asssuming a 8x8 board
getPositions(4, 0, [])
