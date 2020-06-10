# Find total number of unique paths in a maze from source to destination

def isSafe(mat, visited, r, c):
    if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and not visited[r][c] and mat[r][c]:
        return True
    return False


N = 0


def getN(mat, visited, r, c, dest):
    global N
    if r == dest[0] and c == dest[1]:
        N = N + 1
        print("===========DONE==========", N)
        return N

    visited[r][c] = True
    print(r, c)
    if isSafe(mat, visited, r + 1, c):
        # if instead we do return here directly, that vl just print one path
        # but we need all paths, so we need to get to next step too
        count = getN(mat, visited, r + 1, c, dest)
    if isSafe(mat, visited, r - 1, c):
        count = getN(mat, visited, r - 1, c, dest)
    if isSafe(mat, visited, r, c + 1):
        count = getN(mat, visited, r, c + 1, dest)
    if isSafe(mat, visited, r, c - 1):
        count = getN(mat, visited, r, c - 1, dest)
    visited[r][c] = False
    return N


mat = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]
rows = len(mat)
cols = len(mat[0])
V = [[False for i in range(cols)] for j in range(rows)]

getN(mat, V, 0, 0, (rows - 1, cols - 1))
