import sys
sys.stdin = open("1248_공통조상.txt", "r")

def find1(num1):
    if tree[num1][2]:
        parent = tree[num1][2]
        p_list1.append(parent)
        find1(parent)

def find2(num2):
    if tree[num2][2]:
        parent = tree[num2][2]
        p_list2.append(parent)
        find2(parent)

def subtree(v):
    global cnt
    if v == 0:
        return
    cnt += 1
    subtree(tree[v][0])
    subtree(tree[v][1])

T = int(input())
for tc in range(1, T+1):
    V, E, num1, num2 = map(int, input().split())
    line_list = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(E+2)]
    p_list1 = []
    p_list2 = []
    for i in range(E):
        p, c = line_list[i*2], line_list[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    find1(num1)
    find2(num2)
    #parent(0)
    if len(p_list1) < len(p_list2):
        for i in range(len(p_list1)):
            if p_list1[i] in p_list2:
                result = p_list1[i]
                break
    else:
        for i in range(len(p_list1)):
            if p_list2[i] in p_list1:
                result = p_list2[i]
                break
    # print(result)
    # print(p_list1, p_list2)
    cnt = 0
    subtree(result)
    print("#{} {} {}".format(tc, result, cnt))
