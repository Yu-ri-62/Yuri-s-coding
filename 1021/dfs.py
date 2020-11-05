# N = 7
# en = 8
# edges = list(map(int,"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
# #인접행렬 작성하기(adjacency matrix)
# adj = [[0] * (N+1) for _ in range(N+1)]
#
# for i in range(0,len(edges),2):
#     s = edges[i]
#     e = edges[i+1]
#     adj[s][e] = 1
#     adj[e][s] = 1
#
# visited = [0] * (N+1)   # 중복으로 방문하는 것을 막기위해서 방문했음을 표시하기 위한 배열
# result = list()
# #stack을 이용한 dfs
# def dfs(v):
#     stack = list()
#     stack.append(v)
#     visited[v] = 1  # 첫번째 노드는 stack에 추가하면서 방문 표시
#     result.append(v)
#     while stack:
#         current = stack[-1]
#         #현재 노드에서 갈 수 있는 모든 노드 검사
#         visited[current] = 1
#         for i in range(len(adj[current])):
#             #현재 노드와 연결되어 있고 방문하지 않은 노드라면,
#             if adj[current][i] == 1 and visited[i] == 0:
#                 stack.append(i) # 다음방문추가
#                 result.append(i)
#                 break
#         else:   # break에 걸리지 않음 : 현재노드에서 갈수 있는 노드가 없음
#             stack.pop()
# dfs(1)
# print(result)

##################################
#"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int,input().split()))
#인접행렬 작성하기(adjacency matrix)
adj = [[0] * (N+1) for _ in range(N+1)]

for i in range(0,len(edges),2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1

# for row in adj:
#     print(row)

#방문검사 배열이 필요 : visited >> 노드의 길이 + 1
#dfs : 방문 가능한 경로를 만나면 즉시 방문, 경로를 찾을수 없으면 되돌아 감.

visited = [0] * (N+1)
result = list()
def dfs(v):
    global result
    if visited[v]: # 이미 방문한 노드라면 종료
        return
    #방문하지 않는 노드: 나랑 연결되어 있는 모든 노드들을 순회
    result.append(v)    #방문을 했으니 방문 순서에 추가
    visited[v] = 1  # 방문한 노드임을 표시
    #다음 노드들을 검색
    for i in range(len(adj[v])):
        if adj[v][i] == 1:  # [0,0,0,0,1,1,0,0]
            dfs(i)

dfs(1)
print(result)

######################################################33
# 2차원배열 DFS/BFS를 하기 위해서 delta를 이용한 인덱스 접근
# stack/반복문을 이용하여 dfs를 실행하는게 아니라, 재귀를 이용한 dfs 실행
# 2차원 배열의 각각의 요소가 정점(Vertex)이 되는데, 정점들을 구분하기 위해서
# 좌표값을 이용해서 각 정점을 구분해야 한다.
#시작점 2, 도착지점 3, 통로는 1

# (0,1),(1,1), (2,1),(3,1),(3,2),(3,3),(2,3),(1,3),(1,4)
# (1,5),(2,5),(3,5),(4,5),(5,5),(5,4),(5,3),(5,2)
maze = [
[0,2,0,1,0,0],
[0,1,0,1,1,1],
[1,1,0,1,0,1],
[0,1,1,1,0,1],
[1,1,0,0,0,1],
[1,0,3,1,1,1]
]
N = 6
#도착지점까지 이동좌표 출력하기
#스택에 경로를 집어넣어두고, 도착지에 도착하면, 순서대로 출력하면 됨
#경로를 찾아가는 중간에 저장된 경로는 스택에서 빠져나오지 않음
#(잘못된 경로일 경우 =길이 없는 경우에는 스택에서 빠짐)
# 2차원 배열에서 각각의 요소를 구분하기 위해서는 좌표값으로 구분한다.
def dfs(r,c):
    stack = list()
    stack.append((r,c)) #좌표값을 튜플의 형태로 스택에 저장
    # 방문한 좌표의 재방문을 방지하기 위해서 visited 배열 생성
    visited = [[0] * 6 for _ in range(6)]
    visited[r][c] = 1
    #사방 탐색을 위해서 delta 배열 작성
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while stack:
        #스택의 top(최상단)에 있는 요소를 가져옴 (pop 하지 않음)
        top_r,top_c = stack[-1]
        # 가져온 요소에서 갈 수 있는 경로를 탐색 (사방탐색)
        for d in range(4):
            nr = top_r + dr[d]
            nc = top_c + dc[d]
            # 1. 갈 수 있는 경로가 있다면, 스택에 새로운 경로 추가
            if  0 <= nr < N and 0 <= nc < N and maze[nr][nc] and not visited[nr][nc]:
                # 1-1  갈수 있는 경로가 목적지라면, 스택내용 출력
                if maze[nr][nc] == 3:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
                    for e in stack:
                        print(e,end=" ")
                    return
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        # 2. 갈 수 있는 경로가 없다면, 스택의 최상단 요소 삭제(pop)
        else:
            stack.pop()

dfs(0,1)

#######################################
# 2차원배열 DFS/BFS를 하기 위해서 delta를 이용한 인덱스 접근
# 2차원 배열의 각각의 요소가 정점(Vertex)이 되는데, 정점들을 구분하기 위해서
# 좌표값을 이용해서 각 정점을 구분해야 한다.
#시작점 2, 도착지점 3, 통로는 1
# (0,1),(1,1), (2,1),(3,1),(3,2),(3,3),(2,3),(1,3),(1,4)
# (1,5),(2,5),(3,5),(4,5),(5,5),(5,4),(5,3),(5,2)
maze = [
[0,2,0,1,0,0],
[0,1,0,1,1,1],
[1,1,0,1,0,1],
[0,1,1,1,0,1],
[1,1,0,0,0,1],
[1,0,3,1,1,1]
]
N = 6
#도착지점까지 이동좌표 출력하기
#스택에 경로를 집어넣어두고, 도착지에 도착하면, 순서대로 출력하면 됨
#경로를 찾아가는 중간에 저장된 경로는 스택에서 빠져나오지 않음
#(잘못된 경로일 경우 =길이 없는 경우에는 스택에서 빠짐)
# 2차원 배열에서 각각의 요소를 구분하기 위해서는 좌표값으로 구분한다.
# 방문한 좌표의 재방문을 방지하기 위해서 visited 배열 생성
visited = [[0] * 6 for _ in range(6)]
# 사방 탐색을 위해서 delta 배열 작성
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
path = list() #이동경로를 저장
def dfs(r,c):
    visited[r][c] = 1
    path.append((r, c))
    if maze[r][c] == 3: #목적지에 도착
        for e in path:
            print(e,end=" ")
        print()
        return
    # 목적지에 도착하지 않았다면, 갈수 있는 경로를 탐색
    # 사방탐색
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 갈 수 있는 경로가 있다면, 다음 단계로 진행
        #검사하는 좌표가 범위 안에있고, 미로의 통로이고, 방문하지 않음
        if 0 <= nr < N and 0<=nc<N and maze[nr][nc] and visited[nr][nc] == 0:
            dfs(nr,nc)
    #return
    path.pop()
dfs(0,1)