import sys
sys.stdin = open("2050_알파벳을숫자로변환.txt", "r")

T = list(input())
for i in range(len(T)):
    print(ord(T[i])-64, end=" ")