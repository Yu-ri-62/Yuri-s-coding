import sys
sys.stdin = open("1267_작업순서.txt", "r")

T = 2
for tc in range(1,T+1):
    V, E = map(int,input().split())
    edges = list(map(int,input().split()))
    adj = [[0]*(V+1) for _ in range(V+1)]
    #선행작업을 저장하는 행렬
    prev_arr = [[0]*(V+1) for _ in range(V+1)]
    #작업순서를 저장할 리스트
    order_list = list()

    for i in range(0,len(edges),2):
        adj[edges[i]][edges[i+1]] = 1
        prev_arr[edges[i+1]][edges[i]] = 1 #선행작업 저장배열

    #선행작업이 없는 노드들 order_list에 추가
    for i in range(1,len(prev_arr)):
        #선행작업이 없음,
        if prev_arr[i].count(1) == 0:
            order_list.append(i)

    #노드들을 순회하면서, order_list에 넣을지를 결정
    # 선행작업 목록 확인해서, 선행작업들이 모두 order_list에
    # 들어가 있으면, 선행작업이 완료된 상황 >> order_list에 넣음
    # order_list에 모든 노드들이 들어갈 때 까지 반복
    while len(order_list) < V:
        for i in range(1,V+1):
            if i not in order_list: #i 번째 노드 작업하지 않음
                #i번 노드의 선행작업이 모두 이루어졌는지 확인
                #선행작업 prev_arr 확인
                for j in range(1,V+1):
                    #j번작업이 i번 작업의 선행작업인데, j가 order_list에 없으면,
                    if prev_arr[i][j] == 1 and j not in order_list:
                        #i는 작업하면 안됨
                        break
                else: #break가 안걸리면, 선행작업이 완료된 상황
                    order_list.append(i)

    print("#{}".format(tc),*order_list)


###################################################################
#DFS
#아까전 반복문은 선행작업먼저 처리
#이번에는 깊이 우선으로 진행하면서, 후행작업먼저 stack에 넣고
#후행작업이 없으면, 자기 자신을 stack에 넣는다.
def dfs(v):
    visited[v] = 1
    #모든 후행작업 확인 후, 실행하지 않은 후행작업있으면 후행작업부터 탐색
    for i in range(1,V+1):
        if adj[v][i] == 1 and not visited[i]:
            dfs(i)
    #for문이 끝나면, 후행작업을 모두 마친 상태
    stack.append(v)


T = 2
for tc in range(1,T+1):
    V, E = map(int,input().split())
    edges = list(map(int,input().split()))
    #각 행의 인덱스에 해당하는 노드의 후행작업 노드들 표시(인접행렬)
    adj = [[0]*(V+1) for _ in range(V+1)]
    #선행작업을 저장하는 행렬
    prev_arr = [[0]*(V+1) for _ in range(V+1)]

    stack = list() #작업순서 후행으로 먼저 push할 stack
    visited = [0]*(V+1)     #노드 방문여부 체크

    for i in range(0,len(edges),2):
        f,t = edges[i],edges[i+1]   #from/to
        adj[f][t] = 1
        prev_arr[t][f] = 1
    #선행작업이 없는 위치에서 깊이 우선탐색 실행
    for i in range(1,V+1):
        if prev_arr[i].count(1) == 0:   #선행작업 없음
            dfs(i)

    print("#{}".format(tc),*stack[::-1])     # *는 , 없이 값만 나온다.