import sys
sys.stdin = open("1545_거꾸로출력.txt", "r")

T = int(input())
for i in range(T,-1,-1):
    print(i, end=' ')