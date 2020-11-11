import sys
sys.stdin = open("단순2진암호코드.txt", "r")

code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
         '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    board = [[0]*(C+1)] + [[0] + list(map(int, input())) for _ in range(R)]
    for i in range(R):
        if 1 in board[i]:
            start_r = i
            break
    row = board[start_r]

    for j in range(len(row)-1,-1,-1):
        if board[start_r][j] == 1:
            start_c = j-55
            break

    num_list = []
    for l in range(start_c, start_c+56, 7):
        n_code = ''
        for m in range(l, l+7):
            n_code += str(row[m])
        num_list.append(code[n_code])

    sum_odd = 0     # 홀수
    sum_even = 0    # 짝수
    for i in range(0, len(num_list), 2):
        sum_odd += num_list[i+1]
        sum_even += num_list[i]
    test = (sum_even*3) + sum_odd

    if test % 10 == 0:
        print('#{} {}'.format(tc, sum(num_list)))
    else:
        print('#{} {}'.format(tc, '0'))


