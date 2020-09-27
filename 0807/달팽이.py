arr = [[0] * 5 for _ in range(5)]
# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
r = 0  # 상하
c = 0  # 좌우
arr[r][c] = 1

# 우측으로 좌표 이동
r += dr[0]
c += dc[0]
arr[r][c] = 2

r += dr[1]
c += dc[1]
arr[r][c] = 3

# 오른쪽으로 계속 움직이면서 1을 채우다가 영역을 벗어나면 멈추기
r = 0
c = 0
d = 0    # 델타 인덱스, 방향을 결정하는 변수
cnt = 1
while cnt < 25:
    if 0<=r<5 and 0 <= c < 5 and arr[r][c] == 0:       # 영역을 벗어나면, 방향전환
        arr[r][c] = cnt
        cnt += 1
    else:
        c -= dc[d]
        r -= dc[d]
        d = (d+1) % 4     #0,1,2,3만 반복하게 하기 위해서 %4
    r += dr[d]
    c += dr[d]

for row in arr:
    print(*row)