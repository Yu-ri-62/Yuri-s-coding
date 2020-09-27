import sys
sys.stdin = open("2001_파리퇴치.txt", "r")

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for n in range(N):
        numbers = list(map(int, input().split()))
        arr.append(numbers)

    sum_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for r in range(i, i+M):
                for l in range(j, j+M):
                    sum += arr[r][l]
            sum_list.append(sum)
    sum_max = 0
    for i in range(len(sum_list)):
        if sum_list[i] > sum_max:
            sum_max = sum_list[i]
    print("#%d" %tc, sum_max)




