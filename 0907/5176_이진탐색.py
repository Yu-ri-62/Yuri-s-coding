import sys
sys.stdin = open("5176_이진탐색.txt", "r")

def in_order(idx):
    global num
    if idx > N:
        return
    in_order(idx*2)
    my_tree[idx] = num
    num += 1
    in_order(idx*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_tree = [0]*(N+1)
    num = 1
    in_order(1)
    print(my_tree)
    print("#{} {} {}".format(tc, my_tree[1], my_tree[N//2]))

##########################################################
# 풀이
for tc in range(1, int(input()) +1)):
    N = int(input())
    T = [0] * (N+1)
    cnt = 1
    inorder(1)


def inorder(v):
    global cnt
    if v > N:
        return
    inorder(v*2)
    T[v] = cnt
    cnt += 1
    inorder(v*2+1)