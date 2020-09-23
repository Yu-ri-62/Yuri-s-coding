import sys
sys.stdin = open("4835_구간합.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):             # 리스트에서 정해진 길이만큼의 합
        SUM = 0
        for j in range(i, i+M):
            SUM += num_list[j]
        sum_list.append(SUM)
    sum_max = 0
    sun_min = 1000000000000000000000000000000000000000000
    for i in range(len(sum_list)):
        if sum_list[i] > sum_max:
            sum_max = sum_list[i]

        if sum_list[i] < sun_min:
            sun_min = sum_list[i]

    print("#{} {}".format(tc, sum_max-sun_min))