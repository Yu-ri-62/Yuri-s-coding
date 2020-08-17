import sys
sys.stdin = open("2071_평균값구하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    total = 0
    count = 0
    for i in range(len(number)):
        total += number[i]
        count += 1
    print('#%d' %tc, round(total/count))