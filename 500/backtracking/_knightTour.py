rows = [2, 1, -1, -2, -2, -1, 1, 2]
cols = [1, 2, 2, 1, -1, -2, -2, -1]

import pprint as pp


def isValidPos(N, r, c, positions):
    if r < N and c < N and r >= 0 and c >= 0 and (r,c) not in positions:
        return True
    return False


def getTour(N, row, col, positions):
    positions.append((row, col))

    if len(positions) >= N * N:
        print(len(positions), positions)
        return True

    # visit this row, col


    # recur for all possible
    for k in range(8):
        r = rows[k]
        c = cols[k]
        if isValidPos(N, row + r, col + c, positions):
            print(row + r, col + c)
            getTour(N, row + r, col + c, positions)
    # if out of this for, pop from positions
    positions.pop()
    return False

#
# def getPosMatrix(N, positions):
#     pos = [[0 for i in range(N)] for j in range(N)]
#
#     for i in range(N * N):
#         print(i)
#         (r, c) = positions[i]
#         pos[r][c] = i
#     pp.pprint(pos)



getTour(5, 0, 0, [])

# getPosMatrix(4, positions)
