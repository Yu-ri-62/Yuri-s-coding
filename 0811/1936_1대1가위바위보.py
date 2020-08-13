import sys
sys.stdin = open("1936_1대1가위바위보.txt", "r")

A, B = map(int, input().split())
if A > B:
    if A == 3 and B == 1:
        print('B')
    print('A')
else:
    if B == 3 and A == 1:
        print('A')
    print('B')
