import sys
sys.stdin = open("2029_몫과나머지출력하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    print('#%d' %tc, a//b, a%b)