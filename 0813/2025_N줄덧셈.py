import sys
sys.stdin = open("2025_N줄덧셈.txt", "r")

T = int(input())
sum_number = 0
for tc in range(T+1):
    sum_number += tc
print(sum_number)