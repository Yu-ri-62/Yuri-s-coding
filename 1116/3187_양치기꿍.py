import sys
sys.stdin = open("3187_양치기꿍.txt", "r")


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[0]*(C) for _ in range(R)]
rc = [1, -1, 0, 0]
cc = [0, 0, 1, -1]
queue = []
sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        cnt_k = 0
        cnt_v = 0
        if arr[i][j] != '#' and visited[i][j] == 0:
            queue.append((i, j))
            visited[i][j] = 1
            if arr[i][j] == 'k':
                cnt_k += 1
            if arr[i][j] == 'v':
                cnt_v += 1
            while queue:
                r, c = queue.pop(0)
                for n in range(4):
                    nr = r + rc[n]
                    nc = c + cc[n]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != '#' and visited[nr][nc] != 1:
                        if arr[nr][nc] == 'k':
                            cnt_k += 1
                        if arr[nr][nc] == 'v':
                            cnt_v += 1
                        queue.append((nr, nc))
                        visited[nr][nc] = 1
            if cnt_v >= cnt_k:
                wolf += cnt_v
            else:
                sheep += cnt_k
print(sheep, wolf)