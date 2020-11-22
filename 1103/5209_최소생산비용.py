import sys
sys.stdin = open("5209_최소생산비용.txt", "r")


def dfs(row):
    global min_sum, total

    if row == N:
        if min_sum > total:
            min_sum = total
        return

    if total > min_sum:
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                total += arr[row][i]
                visited[i] = 1
                dfs(row+1)
                visited[i] = 0
                total -= arr[row][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 99999999
    total = 0

    dfs(0)
    print("#{} {}".format(tc, min_sum))