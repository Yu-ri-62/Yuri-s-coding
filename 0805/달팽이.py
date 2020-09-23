# 1954. 달팽이 숫자
import sys
sys.stdin = open('달팽이.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    cnt = N*N
    # delta : 우 하 좌 상
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    # delta = [(0,1),(1,0),(0,-1),(-1,0)]

    r = 0   # 가로좌표 0,0 부터 시작
    c = 0   # 세로좌표
    d = 0 # 델타 인덱스
    num = 1 # 증가하는 숫자( 배열에 채울 숫자)
    while num <= cnt:    # 총 N*N개의 숫자를 채워야함
        #벽 이거나, 채울 수 없으면 방향전환
        if 0<= r < N and 0<= c < N and not arr[r][c]:
            arr[r][c] = num
            num += 1
        else:   #범위 벗어남
            r -= dr[d]
            c -= dc[d]
            d = (d+1)%4
        r += dr[d]
        c += dc[d]
    print("#{} ".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()
    # for row in arr:
    #     print(row)


#########################################################3
# # arr= [2 for _ in range(5) ]
# # print(arr)
# arr= [[0] * 5 for _ in range(5)]
# # 우 하 좌 상
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
# r = 0
# c = 0
# # arr[r][c] = 1
# #
# # # 우측으로 좌표 이동
# # r += dr[0]
# # c += dc[0]
# # arr[r][c] = 2
# #
# # r += dr[1]
# # c += dc[1]
# # arr[r][c] = 3
# #
# # for row in arr:
# #     print(*row)
#
# # 오른쪽으로 계속 움직이면서 1채우다가 영역을 벗어나면 멈추기
# r = 0
# c = 0
# d = 0   # 델타 인덱스, 방향을 결정하는 변수
# cnt = 1
# while cnt <= 25:
#     if 0<=r<5 and 0 <= c < 5 and arr[r][c] == 0:
#         arr[r][c] = cnt
#         cnt += 1
#     else:
#         c -= dc[d]
#         r -= dr[d]
#         d = (d + 1) % 4 # 0,1,2,3만 반복하게 하기 위해서 % 4
#     r += dr[d]
#     c += dc[d]
#
# print("끝")
#
# for row in arr:
#     print(*row)