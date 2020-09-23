'''
1 2 3
4 5 6
7 8 9
'''
# 1
N, M = map(int, input().split())
mylist = [0 for _ in range(N)]
#mtlist = [0] * N

for i in range(N):
    mylist[i] = list(map(int, input().split()))
print(mylist)

#2
N, M =map(int, input().split())
mylist = []
for i in range(N):
    mylist.appendlist((map(int, input().split())))
print(mylist)

#3
N, M =map(int, input().split())
mylist[i] = list(map(int, input().split())) for _ in range(N)
print(mylist)

# 0 으로 초기화하는 방법
N = 3  #행
M = 4  #열

#v = [[0 for _ in range(M)] for _ in range(N)]
v = [[0] * M for _ in range(N)]
print(v)



#1
for i in range(N):
    for j in range(M):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
#2
for i in range(N):
    for j in range(i+1, M):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)