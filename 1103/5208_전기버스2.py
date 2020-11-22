import sys
sys.stdin = open("5208_전기버스2.txt", "r")


def bus(station):
    global cnt, min_cnt
    if station >= N:
        if cnt <= min_cnt:
            min_cnt = cnt
        return

    if cnt>=min_cnt:     # 시간초과가 생긴다면 가지치기하기
        return

    else:
        charge = arr[station]
        for i in range(station+charge, station, -1):
            cnt += 1
            bus(i)
            cnt -= 1


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    min_cnt = 99999999
    cnt = 0

    bus(1)
    print("#{} {}".format(tc, min_cnt-1))