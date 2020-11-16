import sys
sys.stdin = open("5202_화물도크.txt", "r")


def work(k):
    global work_cnt
    if k == N-1:
        return work_cnt

    else:
        for i in range(k, k+1):
            for j in range(i+1, N):
                if time[i][0] <= time[j][1]:
                    work_cnt += 1
                    work(j)
                    break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split()))[::-1] for _ in range(N)]
    time.sort()
    work_cnt = 1
    #print(time)

    work(0)
    print("#{} {}".format(tc, work_cnt))