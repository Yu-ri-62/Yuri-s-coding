import sys
sys.stdin = open("2606_바이러스.txt", "r")


com = int(input())
connect = int(input())
arr = [[0] * (com+1) for _ in range(com+1)]
visited = [0] * (com+1)
queue = []
cnt = 0
for _ in range(connect):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1

visited[1] = 1
for i in range(com+1):
    if arr[1][i] == 1 and visited[i] == 0:
        queue.append(i)
        cnt += 1
        visited[i] = 1

while queue:
    a = queue.pop(0)
    for j in range(com+1):
        if arr[a][j] == 1 and visited[j] == 0:
            queue.append(j)
            cnt += 1
            visited[j] = 1
print(cnt)