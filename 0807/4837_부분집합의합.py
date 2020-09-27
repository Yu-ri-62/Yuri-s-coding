import sys
sys.stdin = open("4837_부분집합의합.txt", "r")

T = int(input())
number_list = [i for i in range(1, 13)]
n = len(number_list)
sum_li = []
for i in range(1 << n):
    number_sum = 0
    cnt = 0
    for j in range(n+1):
        if i & (1 << j):
            number_sum += number_list[j]
            cnt += 1
    sum_li += [{number_sum:cnt}]

for tc in range(T):
    total = 0
    N, K = map(int, input().split())
    for i in range(len(sum_li)):
        for a, b in sum_li[i].items():
            if K == a and N == b:
                total += 1
    print('#{} {}'.format(tc+1, total))