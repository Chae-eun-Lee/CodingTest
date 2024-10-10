
board = {}
n1, m1 = input().split()
n,m = int(n1), int(m1)

for i in range(m):
    u, v = input().split()
    if u not in board:
        board[u] = [v]
    else:
        board[u].append(v)
    if v not in board:
        board[v] = [u]
    else:
        board[v].append(u)
def dfs_path(board, start, goal, path=None, paths=None):
    if path is None:
        path = []
    if paths is None:
        paths = []
    path.append(start)

    if start == goal:
        paths.append(list(path))
    else:
        for neighbor in board[start]:
            if neighbor not in path:
                dfs_path(board, neighbor, goal, path, paths)

    path.pop()

    return paths

answer = 0
for j in range(1, n):
    ever = True
    s = str(j)
    if s not in board:
        continue

    all_path = dfs_path(board, s, str(n))
    for p in all_path:
        if len(p)%2 == 1:
            ever = False
            break
    if ever:
        answer += 1

print(answer*n)