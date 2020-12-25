import sys
sys.stdin = open("3187_양치기꿍.txt", "r")


dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

for _ in range(100):
    w, h = map(int, input().split())
    if w != 0:
        arr = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0
        for i in range(h):     # 시작점찾기
            for j in range(w):
                stack = []
                #visited = []
                if arr[i][j] == 1:   # 시작!
                    stack.append((i, j))   # 스택에 시작점 append
                    while stack:           # 스택이 비어있지 않다면
                        r = stack[-1][0]   # 스택의 탑을 먼저 확인
                        c = stack[-1][1]
                        stack.pop(-1)
                        for k in range(8): # 8방을 돌아보면서 길을 찾음.
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:  # 범위안에 있고 1이라면
                                stack.append((nr, nc))   # 스택에 넣기기
                        arr[r][c] = 0 # 방문 표시
                    cnt += 1

    else:
        break
    print(cnt)