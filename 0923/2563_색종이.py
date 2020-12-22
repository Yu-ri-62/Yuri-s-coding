import sys
sys.stdin = open("2563_색종이.txt", "r")

N = int(input())
board = [[0]*100 for _ in range(100)]
for i in range(N):
    left, under = map(int, input().split())
    for i in range(left, left+10):
        for j in range(100-under-10, 100-under):
            if 0<= i <100 and 0<= j <100:
                board[i][j] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] != 0:
            cnt +=1
print(cnt)

#################################################
#풀이
num = int(input())
li = [[0] * 100 for _ in range(100)]

for i in range(num):
    a, b = map(int, input().split())

    for r in range(a, a+10):   # a a+1 a+2 a+3 a+4 a+5 a+6 a+7 a+8 a+9
        for c in range(b, b+10):
            li[r][c] = 1
area = 0
for i in range(100):
    for j in range(100):
        area += li[i][j]

print(area)