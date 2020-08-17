import sys
sys.stdin = open("2072_홀수만더하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    number_sum = 0
    for i in range(len(number)):
        if number[i] % 2 == 1:
            number_sum += number[i]
    print('#%d' %tc ,number_sum)