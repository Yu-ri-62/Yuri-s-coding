import sys
sys.stdin = open("10157_자리배정.txt", "r")

C, R = map(int, input().split())
number = int(input())
seat = [[0]*C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = C*R
r = R-1
c = 0
d = 0
num = 1
while num <= cnt:
    if 0<= r < R and 0<= c < C and seat[r][c] == 0:
        seat[r][c] = num
        num += 1
    else:
        r -= dr[d]
        c -= dc[d]
        d = (d+1)%4
    r += dr[d]
    c += dc[d]
if number > cnt:
    print(0)
for i in range(R):
    for j in range(C):
        if seat[i][j] == number:
            print(j+1, R-i)