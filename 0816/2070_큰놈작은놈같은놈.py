import sys
sys.stdin = open("2070_큰놈작은놈같은놈.txt", "r")

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        print('#%d' %tc, '>')
    elif a < b:
        print('#%d' %tc, '<')
    else:
        print('#%d' %tc, '=')