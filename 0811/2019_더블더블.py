import sys
sys.stdin = open("2019_더블더블.txt", "r")

T = int(input())
for i in range(T+1):
    if i == 0:
        print(1, end=" ")
    else:
        print(2**i, end=" ")