"1 2, 1 3, 2 4, 2 5, 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int,"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
#인접행렬 작성하기(adjacency matrix)
adj = [[0] * (N+1) for _ in range(N+1)]
for i in range(0,len(edges),2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1
visited = [0] * (N+1)   # 중복으로 방문하는 것을 막기위해서 방문했음을 표시하기 위한 배열
result = list()
#queue을 이용한 bfs
def bfs(v):
    # 지나오면서 가능한 경로를 확인해 두고, 확인한 순서대로 방문
    # 먼저 확인한 경로를 먼저 방문 >> FIFO (First In First Out)  : Queue 가 적합
    queue = list()
    queue.append(v)
    visited[v] = 1  # queue에 추가하면서 방문했음을 표시
    result.append(v)

    while queue:
        # queue에 들어있는 요소중, 가장 먼저 삽입된 요소를 확인
        head = queue.pop(0)
        # 방문가능한 경로를 확인하면서,
        for i in range(len(adj[head])):
            # 방문가능한 경로를 찾으면 queue에 삽입
            if adj[head][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                result.append(i)

bfs(1)
print(result)

###################################

# 2차원배열 DFS/BFS를 하기 위해서 delta를 이용한 인덱스 접근
# stack/반복문을 이용하여 dfs를 실행하는게 아니라, 재귀를 이용한 dfs 실행
# 2차원 배열의 각각의 요소가 정점(Vertex)이 되는데, 정점들을 구분하기 위해서
# 좌표값을 이용해서 각 정점을 구분해야 한다.
#시작점 2, 도착지점 3, 통로는 1

maze = [
[0,2,0,1,0,0],
[0,1,0,1,1,1],
[1,1,0,1,0,1],
[0,1,1,1,0,1],
[1,1,0,0,0,1],
[1,0,3,1,1,1]
]
N = 6
#도착지점까지 거리구하기
def bfs(r,c):
    # 방문한 좌표의 재방문을 방지하기 위해서 visited 배열 생성
    visited = [[0] * 6 for _ in range(6)]
    visited[r][c] = 1
    #사방 탐색을 위해서 delta 배열 작성
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    queue = list()
    # 시작지점은 시작점으로 부터 0만큼 떨어져 있으니 0부터 시작
    queue.append((r,c,0))
    # 목적지까지의 거리를 구하기 위해서,
    # 현재 검사하는 위치가 시작지점으로 부터 얼마나 떨어졌는가?
    # 시작점으로 부터 이동가능한 좌표를 검사하고 queue에 넣을건데
    # 방금 검사한 좌표의 거리에다가 +1을해서 넣어주면 된다.
    while queue:
        cr,cc,cnt = queue.pop(0)
        if maze[cr][cc] == 3:
            return cnt
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<= nr < N and 0<=nc <N and maze[nr][nc] and not visited[nr][nc]:
                queue.append((nr,nc,cnt+1))
                visited[nr][nc] = 1

result = bfs(0,1)
print(result)