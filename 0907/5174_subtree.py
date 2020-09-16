import sys
sys.stdin = open("5174_subtree.txt", "r")

def subtree(node):
    global cnt
    if node != 0:
        cnt += 1
        subtree(tree[node][0])
        subtree(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    line = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(E+2)]
    cnt = 0
    for i in range(E):
        p, c = line[i*2], line[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    subtree(N)
    print("#{} {}".format(tc, cnt))

#############################################
# 풀이
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 정점 번호 1 ~ E+1
    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)

    arr = list(map(int, input().split()))
    for i in range(0, E+2, 2):   # arr[i] ---> arr[i+1]
        p, c = arr[i], arr[i+1]

        if L[p]:   # p의 왼쪽자식이 있으면
            R[p] = c
        else:
            L[p] = c
        P[c] = p
    ans = 0
    def traverse(v):
        if v == 0:
            return
        ans += 1
        traverse(L[v])
        traverse(R[v])

    traverse(N)
    print(ans)


# return사용
for tc in range(1, T+1):
    E, N = map(int, input().split())

    # 정점 번호 1 ~ E+1
    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)

    arr = list(map(int, input().split()))
    for i in range(0, E+2, 2):   # arr[i] ---> arr[i+1]
        p, c = arr[i], arr[i+1]

        if L[p]:   # p의 왼쪽자식이 있으면
            R[p] = c
        else:
            L[p] = c
        P[c] = p
    ans = 0
    def traverse(v):
        if v == 0:
            return 0
        l = traverse(L[v])
        r = traverse(R[v])
        return l + r + 1

    print(traverse(N))