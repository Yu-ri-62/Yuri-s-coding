import sys
sys.stdin = open("4828_minmax.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    number_list = list(map(int, input().split()))
    for i in range(len(number_list)-1, 0, -1):
        for j in range(i):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    min_max = number_list[-1] - number_list[0]
    print("#{} {}".format(tc, min_max))
