import sys
sys.stdin = open("2819_격자판의숫자이어붙이기.txt", "r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]
#r,c는 현재좌표
#cnt 현재까지 연결한 숫자 개수
#number 현재까지 연결된 중간결과
def dfs(r,c,cnt,number):
    if cnt == 6:    #숫자 7개를 모두 만들었으면, 더 이상 재귀호출 X
        result.add(number)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr < N and 0 <= nc < N:
            new_number = number + board[nr][nc]
            dfs(nr,nc,cnt+1,new_number)

T = int(input())
for tc in range(1,T+1):
    N = 4
    board = [input().split() for _ in range(N)]
    result = set()  #중복되지 않는 숫자만 저장하면 된다.
    #모든 칸이 시작점이 되는 경우를 고려한다.
    for i in range(N):
        for j in range(N):
            dfs(i,j,0,board[i][j])

    print("#{} {}".format(tc,len(result)))