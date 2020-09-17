import sys
sys.stdin = open("3752_가능한시험점수.txt", "r")

def dfs(k, s):
    if visit[k][s]:
        return
    visit[k][s] = 1
    if k == N:
        return
    else:
        dfs(k+1, s)      # k번 문제를 틀린경우
        dfs(k+1, s+score[k])      # k번 문제 맞은 경우
        return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = [[0]*(sum(score)+1) for _ in range(N+1)]  # 마지막에 중복을 제거하기 위해
    dfs(0, 0)
    print("#{} {}".format(tc, sum(visit[N])))