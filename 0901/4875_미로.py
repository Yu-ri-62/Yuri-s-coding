import sys
sys.stdin = open("4875_미로.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        row = list(map(int, input()))
        arr.append(row)
    dr = [0, -1, 0, 1]   # 우, 상, 좌, 하
    dc = [1, 0, -1, 0]
    result = 0
    #print(arr)
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                visited = [[0]*N for _ in range(N)]
                stack = []
                stack.append((r, c))
                while stack:
                    nr, nc = stack.pop()
                    visited[nr][nc] = 1
                    for d in range(len(dr)):
                        sr = nr + dr[d]
                        sc = nc + dc[d]
                        if 0<= sr <N and 0<= sc < N and arr[sr][sc] !=1 and visited[sr][sc] ==0:
                            stack.append((sr, sc))
                            visited[sr][sc] = 1
                            if arr[sr][sc] == 3:
                                result = 1
                                break
                print("#{} {}".format(tc, result))



