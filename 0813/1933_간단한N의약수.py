import sys
sys.stdin = open("1933_간단한N의약수.txt", "r")

T = int(input())
for number in range(1, T+1):
    if T % number == 0:
        print(number, end=" ")
