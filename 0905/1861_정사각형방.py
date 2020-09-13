import sys
sys.stdin = open("1861_정사각형방.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split()))  for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = []
    visited = [[0] * N for _ in range(N)]
    cnt = 1
    cnt_list = []
    for i in range(N):
        for j in range(N):
            start = room[i][j]
            visited[i][j] = 1
            r, c = i, j
            queue.append((r, c, cnt))
            while queue:
                cr, cc, count = queue.pop(0)
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                        if room[cr][cc]+1 == room[nr][nc]:
                            queue.append((nr, nc, count+1))

            cnt_list.append((count,start))
            cnt_list.sort(reverse=True, key=lambda x:x[0])
            max = 0
            for m in range(len(cnt_list)):
                if cnt_list[m][0] > max:
                    max = cnt_list[m][0]
                    min_start = cnt_list[m]


    print("#{} {} {}".format(tc, min_start[1], min_start[0]))

#############################################################################
# 풀이

def bfs(r,c):
    global max_length,room_num
    queue = list()
    queue.append((r,c))
    cnt = 1
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    #사방 검사를 했을때, 현재 방보다 1작은 방이 사방 중에 있으면
    #검사를 하지 않아도 된다...
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if room[nr][nc] == room[r][c] - 1:
                return

    while queue:
        cr,cc = queue.pop()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<= nr < N and 0<=nc <N:
                if room[nr][nc] == room[cr][cc] + 1:
                    queue.append((nr,nc))
                    cnt += 1
                    break

    if cnt > max_length:
        max_length = cnt
        room_num = room[r][c]
    elif cnt == max_length:
        if room_num > room[r][c]:
            room_num = room[r][c]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    #시작점을 어디서 시작해야할지 모르기때문에  모든 지점을 시작점으로 고려
    max_length = 0
    room_num = N * N
    for i in range(N):
        for j in range(N):
            bfs(i,j)

    print("#{} {} {}".format(tc,room_num,max_length))