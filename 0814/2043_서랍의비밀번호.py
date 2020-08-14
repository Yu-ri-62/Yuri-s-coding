import sys
sys.stdin = open("2043_서랍의비밀번호.txt", "r")

P, K = map(int, input().split())
cnt = 1
while K != P:
    if K < P:
        K += 1
        cnt += 1
print(cnt)