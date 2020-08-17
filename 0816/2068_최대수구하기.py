import sys
sys.stdin = open("2068_최대수구하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    number_max = 0
    for i in range(len(number)):
        if number[i] > number_max:
            number_max = number[i]
    print('#%d' %tc, number_max)