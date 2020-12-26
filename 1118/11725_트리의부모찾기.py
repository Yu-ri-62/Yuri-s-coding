import sys
sys.stdin = open("11725_트리의부모찾기.txt", "r")
sys.setrecursionlimit(10**6)  # python의 경우 재귀를 1000번밖에 못돌리기때문에 limit을 늘려준다.

def tree(v):
    global visited, parent, arr

    for p in range(len(arr[v])):
        if visited[arr[v][p]] == 0:
            parent[arr[v][p]] = v
            visited[arr[v][p]] = 1
            tree(arr[v][p])


N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
parent = [0]*(N+1)
visited = [0]*(N+1)
visited[1] = 1

for i in range(N-1):
    n, m = map(int, sys.stdin.readline().split())
    arr[n].append(m)
    arr[m].append(n)

for j in range(len(arr[1])):
    parent[arr[1][j]] = 1
    visited[arr[1][j]] = 1
    tree(arr[1][j])

for i in range(2, len(parent)):
    print(parent[i])



