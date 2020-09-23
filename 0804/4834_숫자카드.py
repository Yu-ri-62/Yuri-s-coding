import sys
sys.stdin = open("4834_숫자카드.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    cnt_list = [0]*10
    for i in range(N):
        cnt_list[card[i]] += 1
    max_card = 0
    max_index = 0
    for i in range(len(cnt_list)):
        if cnt_list[i] >= max_card:
            max_card = cnt_list[i]
            max_index = i
    print("#{} {} {}".format(tc, max_index, max_card))

