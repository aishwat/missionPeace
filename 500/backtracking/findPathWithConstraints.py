# Find path from source to destination in a matrix that satisfies given constraints

def isSafe(mat, visited, r, c):
    # print("checking ", r, c)
    if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and not visited[r][c]:
        return True
    return False


def findPath(mat, r, c, destination, visited):
    if r == destination[0] and c == destination[1]:
        print("=============AT DESTINATION==========")
        return True
    visited[r][c] = True
    print(r, c)
    k = mat[r][c]

    if isSafe(mat, visited, r - k, c):
        return findPath(mat, r - k, c, destination, visited)
    if isSafe(mat, visited, r, c - k):
        return findPath(mat, r, c - k, destination, visited)
    if isSafe(mat, visited, r, c + k):
        return findPath(mat, r, c + k, destination, visited)
    if isSafe(mat, visited, r + k, c):
        return findPath(mat, r + k, c, destination, visited)

    # backtrack
    visited[r][c] = False
    return False


mat = [
    [7, 1, 3, 5, 3, 6, 1, 1, 7, 5],
    [2, 3, 6, 1, 1, 6, 6, 6, 1, 2],
    [6, 1, 7, 2, 1, 4, 7, 6, 6, 2],
    [6, 6, 7, 1, 3, 3, 5, 1, 3, 4],
    [5, 5, 6, 1, 5, 4, 6, 1, 7, 4],
    [3, 5, 5, 2, 7, 5, 3, 4, 3, 6],
    [4, 1, 4, 3, 6, 4, 5, 3, 2, 6],
    [4, 4, 1, 7, 4, 3, 3, 1, 4, 2],
    [4, 4, 5, 1, 5, 2, 3, 5, 3, 5],
    [3, 6, 3, 5, 2, 2, 6, 4, 2, 1]
]
N_R = len(mat)
N_C = len(mat[0])
V = [[False for i in range(N_C)] for j in range(N_R)]
print(N_R, N_C)
print(print(len(V), len(V[0])))

findPath(mat, 0, 0, (N_R - 1, N_C - 1), V)
