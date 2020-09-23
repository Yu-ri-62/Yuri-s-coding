import sys
sys.stdin = open('1209_sum.txt','r')

for tc in range(1, 11):
    x = int(input())
    number_list = []
    for num in range(100):
        numbers = list(map(int, input().split()))
        number_list.append(numbers)

    max_number = 0
    for i in range(100):
        row_sum = 0
        column_sum = 0
        for j in range(100):
            row_sum += number_list[i][j]
            column_sum += number_list[j][i]
        if max_number < row_sum:
            max_number = row_sum
        if max_number < column_sum:
            max_number = column_sum

    cross_sum = 0
    cross_sum2 = 0
    for i in range(100):
        cross_sum += number_list[i][i]
        cross_sum2 += number_list[i][99 - i]
    if max_number < cross_sum:
        max_number = cross_sum
    if max_number < cross_sum2:
        max_number = cross_sum2

    print("#%d" %tc, max_number)