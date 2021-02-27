import sys
sys.stdin = open("18405_경쟁적전염.txt", "r")
from collections import deque


def virous():
    global cnt, S, X, Y, N, infp
    for i in range(N):
        for j in range(N):
            if info[i][j] != 0:
                queue.append((info[i][j], i, j, 0))
    print(queue)
    queue(sorted(queue))
    print(queue)
    while queue:
        num, r, c, cnt = queue.popleft()
        if cnt == S:
            return
        for n in range(4):
            nr = r + dr[n]
            nc = c + dc[n]
            if 0 <= nr < N and 0 <= nc < N and info[nr][nc] == 0:
                queue.append((num, nr, nc, cnt+1))
                info[nr][nc] = num



N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
queue = deque([])
cnt = 0

virous()
print(info[X - 1][Y - 1])