import sys
sys.stdin = open("5207_이진탐색.txt", "r")

def binary(l, r, m, i):
    global cnt
    # for i in range(M):
    if B[i] == A[m]:
        cnt += 1
    else:
        if B[i] < A[m]:
            r = m-1
            m = (l + r)//2
            if B[i] > A[m]:
                binary(l, r, m, i)
            elif B[i] == A[m]:
                cnt += 1

        elif B[i] > A[m]:
            l = m+1
            m = (l + r)//2
            if B[i] < A[m]:
                binary(l, r, m, i)
            elif B[i] == A[m]:
                cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0

    l = 0
    r = N-1
    m = (l+r)//2

    for i in range(M):
        binary(l, r, m, i)

    print("#{} {}".format(tc, cnt))
