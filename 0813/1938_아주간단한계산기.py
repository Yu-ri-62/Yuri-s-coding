import sys
sys.stdin = open("1938_아주간단한계산기.txt", "r")

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))