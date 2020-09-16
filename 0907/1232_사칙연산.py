import sys
sys.stdin = open("1232_사칙연산.txt", "r")

def post_order(idx):
    if tree[idx][0] != 0:
        post_order(tree[idx][1])
        post_order(tree[idx][2])
        if tree[idx][0] == '+':
            tree[idx][0] = tree[tree[idx][1]][0] + tree[tree[idx][2]][0]
        if tree[idx][0] == '-':
            tree[idx][0] = tree[tree[idx][1]][0] - tree[tree[idx][2]][0]
        if tree[idx][0] == '*':
            tree[idx][0] = tree[tree[idx][1]][0] * tree[tree[idx][2]][0]
        if tree[idx][0] == '/':
            tree[idx][0] = tree[tree[idx][1]][0] / tree[tree[idx][2]][0]

T = 10
for tc in range(1, T+1):
    N = int(input())
    node_info = [[0, 0, 0, 0]] +[list(input().split()) for _ in range(N)]
    tree = [[0]*3 for _ in range(N+1)]
    for i in range(N+1):
        if len(node_info[i]) == 4:
            tree[i][0] = node_info[i][1]
            tree[i][1] = int(node_info[i][2])
            tree[i][2] = int(node_info[i][3])
        else:
            tree[i][0] = int(node_info[i][1])
    post_order(1)
    print("#{} {}".format(tc, int(tree[1][0])))


##############################################################################
# 풀이
for tc in range(1, T+1):
    N = int(input())
    T = [[]]

    for i in range(N):
        T.append(list(input().split()))
        if len(T[i]) == 4:    # 연산자
            T[i][2] = int(T[i][2])
            T[i][3] = int(T[i][3])
        else:                 # 피연산자
            T[i][1] = int(T[i][1])
    print(calc(1))

def calc(v):
    if len(T[v]) == 2:  # 피연산자 = 단말노드
        return T[v][1]
    else:               # 연산자
        l = calc(T[v][2])
        r = calc(T[v][3])
        if T[v][1] == '+':
            return l+r
        elif T[v][1] == '-':
            return l-r
        elif T[v][1] == '*':
            return l*r
        else:
            return l/r