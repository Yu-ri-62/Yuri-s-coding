import sys
sys.stdin = open("4836_색칠하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    cnt = 0
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                arr[j][k] += color
    for i in range(10):
        for j in range(10):
            if arr[i][j] ==3:
                cnt += 1
    print("{} {}".format(tc, cnt))
