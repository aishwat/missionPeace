# simple dfs, with lil modification
# need to explore all possible paths


maxDist = []


def isValid(N, visited, mat, i, j):
    if 0 <= i < N and 0 <= j < N and not visited[i][j] and mat[i][j] == 1:
        return True
    return False


def getLongestRoute(mat, visited, i, j, dest_i, dest_j, dist):
    global maxDist
    visited[i][j] = True

    if i == dest_i and j == dest_j:
        visited[i][j] = False
        print("----------")
        print(i, j, dist)
        print("----------")
        print()
        maxDist.append(dist)
        return dist

    # top
    if isValid(N, visited, mat, i - 1, j):
        print(i - 1, j)
        getLongestRoute(mat, visited, i - 1, j, dest_i, dest_j, dist + 1)
    # left
    if isValid(N, visited, mat, i, j - 1):
        print(i, j - 1)
        getLongestRoute(mat, visited, i, j - 1, dest_i, dest_j, dist + 1)

    # right
    if isValid(N, visited, mat, i, j + 1):
        print(i, j + 1)
        getLongestRoute(mat, visited, i, j + 1, dest_i, dest_j, dist + 1)

    # bottom
    if isValid(N, visited, mat, i + 1, j):
        print(i + 1, j)
        getLongestRoute(mat, visited, i + 1, j, dest_i, dest_j, dist + 1)

    print("bactracking", i, j)
    visited[i][j] = False  # <--imp otherwise misses some paths
    return dist  # <-- end up here, means none of the cell is valid, return whatever dist was passed to this cell itself


N = 4
mat = [
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]
visited = [[False for i in range(N)] for j in range(N)]
getLongestRoute(mat, visited, 0, 0, 2, 2, 0)
print(max(maxDist))
# N = 10
# mat = [
#     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
#     [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
# ]
# visited = [[False for i in range(N)] for j in range(N)]
# getLongestRoute(mat, visited, 0, 0, 5, 7, 0)
# print(max(maxDist))
