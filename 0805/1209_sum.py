import sys
sys.stdin = open('1209_sum.txt','r')

T = 10
for tc in range(1, T+1):
    x = int(input())
    number_list = []
    for num in range(100):
        numbers = list(map(int, input().split()))
        number_list.append(numbers)
    #print(number_list)
    N = len(number_list)
    M = len(number_list)
    max_number = 0
    for i in range(N):
        row_sum = 0
        for j in range(M):
            row_sum += number_list[i][j]
        if max_number < row_sum:
            max_number = row_sum

    for j in range(M):
        column_sum = 0
        for i in range(N):
            column_sum += number_list[i][j]
        if max_number < column_sum:
            max_number = column_sum
    cross_sum = 0
    for i in range(M):
        cross_sum += number_list[i][i]
        if max_number < cross_sum:
            max_number = cross_sum

    cross_sum2 = 0
    for i in range(M):
        cross_sum2 += number_list[i][99-i]
        if max_number < cross_sum2:
            max_number = cross_sum2
    print("#%d" %tc, max_number)