import sys
sys.stdin = open("10158_개미.txt", "r")

def solution():
    # 입력
    N, M = map(int, input().split())
    x, y = map(int, input().split())
    t = int(input())
    # t 시간을 변경
    tx, ty = t%(N*2), t%(M*2)
    # 델타 처럼 만들기
    dx, dy = 1, 1
    # tx 시간만큼 이동할 거고
    for i in range(tx):
        if x == N or x == 0: dx *= -1
        x += dx
    # ty 시간만큼 이동할 거야.
    for i in range(ty):
        if y == 0 or y == M: dy *= -1
        y += dy
    print(x, y)
solution()