import sys
sys.stdin = open("1231_중위순회.txt", "r")


def in_order(idx):
    if len(my_tree[idx]) >= 3:
        # 왼쪽
        in_order(idx * 2)
        # 부모
        print(my_tree[idx][1], end="")
        # 오른쪽
        if len(my_tree[idx]) == 4:
            in_order(idx * 2 + 1)
    else:
        print(my_tree[idx][1], end="")

T = 10
for tc in range(1, T+1):
    N = int(input())
    my_tree =[[0, 0, 0, 0]] +[list(input().split()) for _ in range(N)]
    print("#{}".format(tc), end=" ")
    in_order(1)
    print()

#########################################
# # 풀이
# def in_order(v):
#     if v > N:
#         return
#     in_order(v*2)
#     print(tree[v],end="")
#     in_order(v*2+1)
#
# T = 10
# for tc in range(1,T+1):
#     N = int(input())
#     tree = [0] * (N+1)
#     for i in range(1,N+1):
#         info = input().split()
#         tree[i] = info[1]
#
#
#     print("#{}".format(tc),end=" ")
#     in_order(1)
#     print()
