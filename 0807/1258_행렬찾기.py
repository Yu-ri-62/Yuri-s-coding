import sys
sys.stdin = open("1258_행렬찾기.txt", "r")

T = int(input())
for tc in range(T):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    area = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                x = 0
                for k in range(j, n):
                    if matrix[i][k]:
                        x += 1
                    else:
                        break
                y = 0
                for k in range(i, n):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break

                for k in range(i, i + y):
                    for l in range(j, j + x):
                        matrix[k][l] = 0

                area.append([y, x, y * x])
