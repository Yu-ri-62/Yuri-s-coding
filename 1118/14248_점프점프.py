import sys
sys.stdin = open("14248_점프점프.txt", "r")
from collections import deque


def bfs(s):
    global cnt

    queue.append(s)
    visited[s] = 0
    while queue:
        r = queue.popleft()
        nr_1 = r + load[r]
        nr_2 = r - load[r]

        if 0 < nr_1 <= N and visited[nr_1] != 0:
            queue.append(nr_1)
            visited[nr_1] = 0
            cnt += 1

        if 0 < nr_2 <= N and visited[nr_2] != 0:
            queue.append(nr_2)
            visited[nr_2] = 0
            cnt += 1

    return cnt


N = int(input())
load = [0] + list(map(int, input().split()))
visited = [1] * (N+1)
start = int(input())
queue = deque([])
cnt = 1

bfs(start)
print(cnt)