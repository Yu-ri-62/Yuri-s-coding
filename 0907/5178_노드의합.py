import sys
sys.stdin = open("5178_노드의합.txt", "r")

def heap_sum(idx):
    if idx > N+1:
        return 0
    if tree[idx]: # 값이 있다면
        return tree[idx]
    child1 = idx*2
    child2 = idx*2+1
    tree[idx] = heap_sum(child1) + heap_sum(child2)
    return tree[idx]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+2)]
    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    result = heap_sum(L)
    print("#{} {}".format(tc, result))

#####################################################
# 풀이

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    T = [0] * (N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        T[num] = val      # 단말노드 값이 채워짐
    dfs(1)
    print(T[L])

def dfs(v):
    if v > N:
        return 0   # return T[v]를 리턴받기 때문에 0이 필요함
    l = dfs(v*2)
    r = dfs(v*2+1)
    T[v] += l + r    # 단말노드의 값이 변하지 않게 하기 위해서 덮어씌어지는 = 이 아니라 더해주는 += 를 쓴다
    return T[v]

# 함수 대신 for문 사용
    for i in range(N-M, 0, -1): # 배열의 인덱스이자, 노드번호
        T[i] = T[i*2]
        if i * 2 + 1 <= N:
            T[i] += T[i*2+1]