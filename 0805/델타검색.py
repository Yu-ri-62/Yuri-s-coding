arr = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]
      ]

N = len(arr)
M = len(arr[0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(N):
    for y in range(M):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if testX >= 0 and testX < N and testY >= 0 and testX < M: #인덱스 체크
            #if 0 <= testX < N and 0 <= testY < M:  파이썬만 가능
                print(arr[testX][testY], end= " ")



###################################################################3

# delta : 원하는 순서대로 2차원 배열을 순회하기 위해서 사용
# 상하좌우 순서로 접근할 수 있는 델타
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
#     c0     c1    c2
# r0 [0,0] [0,1] [0,2]
# r1 [1,0] [1,1] [1,2]
# r2 [2,0] [2,1] [2,2]
# [1][2][3]
# [4][5][6]
# [7][8][9]
#팔방 시계방향 순회
# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]



arr = [[1,2,3],[4,5,6],[7,8,9]]
r = 1
c = 1
# print(arr[r][c])
# r += dr[0]
# c += dc[0]
# print(arr[r][c])
#상하좌우 연속으로 순회하기
sum_v = 0
for i in range(4):
    #다음좌표를 계산
    nr = r + dr[i]
    nc = c + dc[i]
    sum_v += arr[nr][nc]
print(sum_v)
#팔방 순회 순서는 12시 방향부터 시계방향으로 순회하면서 출력
# 2 3 6 9 8 7 4 1
r = 1
c = 1
for i in range(8):
    nr = r + dr[i]
    nc = c + dc[i]
    print(arr[nr][nc],end=" ")



# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j])