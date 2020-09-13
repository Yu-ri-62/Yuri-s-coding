import sys
sys.stdin = open("7465_창용마을무리의개수.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        arr[s][e] = arr[e][s] = 1                # 간선이 이어진 arr 만들기
    visited = [0]*(N+1)                          # 방문체크를 위해 visited 만들기
    queue = []
    cnt = 0
    for i in range(1, N+1):                      # 노드를 하나씩 돌려본다
        queue.append(i)                          # 노드를 q에 저장  (다른 곳이랑 이어지지 않은 노드도 카운트해야하기 때문에 2차원배열형식이 아닌 노드만 저장하면 된다)
        if visited[i] == 0 :                     # 노드가 방문하지 않았던 곳이라면  (지나왔던 곳은 방문체크가 되어있기 때문에 다시 들어가지 않는다.)
            visited[i] = 1                       # 방문체크를 하고
            while queue:                         # 그리고 q가 있을 때
                node = queue.pop(0)              # q를 pop해서 node에 할당
                for j in range(N+1):             #
                    if arr[node][j] ==1 and visited[j] ==0:    # 들어온 node와 연결되어 있고, 방문하지 않았던 곳이면
                        queue.append(j)                        # q에 저장
                        visited[j] = 1                         # 방문체크
            cnt += 1
    print("#{} {}".format(tc, cnt))


##################################################
# 풀이
def dfs(n):
    stack = list()
    stack.append(n)
    visited[n] = 1
    while stack:
        cur = stack[-1]
        #현재 노드에서 연결된 모든 사람 찾기
        # is_find = False
        for i in range(1,N+1):
            #현재 사람과 연결되어있고, 방문하지 않았다면 방문
            if adj[cur][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = 1
                # is_find = True
                break
        else:
            stack.pop()  # 현재노드 stack에서 삭제
        # if not is_find:
        #     stack.pop() #현재노드 stack에서 삭제


T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    visited = [0]*(N+1)
    result = 0
    for i in range(1,N+1):
        # i번 사람부터 시작해서 연결되는 모든 무리를 순회
        #dfs,bfs
        if not visited[i]:
            dfs(i)
            result += 1
    print("#{} {}".format(tc,result))