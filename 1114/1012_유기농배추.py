import sys
sys.stdin = open("1012_유기농배추.txt", "r")


dr = [0, 0, -1, 1] # 좌 우 상 하
dc = [-1, 1, 0, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())       # M:가로길이, N:세로길이, K:배추위치갯수
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):                        # arr에 1 표시
        c, r = map(int, input().split())
        arr[r][c] = 1
    cnt = 0                 # 지렁이 갯수 셀 변수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:                # 배추밭 시작!
                stack = []
                stack.append((i, j))          # 배추밭 시작점 스택에 저장
                while stack:                  # 스택이 비어있지 않으면
                    r, c = stack.pop()        # 스택의 top을 뽑아서 r, c로 저장
                    for n in range(4):        # 사방을 돌면서
                        nr = r + dr[n]
                        nc = c + dc[n]
                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:     # 범위안에 있고 1이라면
                            stack.append((nr, nc))                               # 스택에 저장
                    arr[r][c] = 0               # 처음에 들어온 곳에 방문 표시
                cnt += 1                # 지렁이 갯수 더해주기
    print(cnt)