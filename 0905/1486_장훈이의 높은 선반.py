import sys
sys.stdin = open("1486_장훈이의 높은 선반.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    list_sum = []
    for i in range(1, 2**N):
        sum = 0
        for j in range(N):
            if i & 1 << j:
                sum += arr[j]
                list_sum.append(sum)
    INF = float('inf')
    min_sum = INF
    for i in range(len(list_sum)):
        if list_sum[i] >= B:
            if min_sum > list_sum[i]:
                min_sum = list_sum[i]
    print("#{} {}".format(tc,min_sum-B))


#######################################################
# 풀이


def tower(idx,tmp_sum):
    global min_height
    if tmp_sum > min_height:
        return
    if idx == N:
        #키의 합이 B가 넘는 경우에만 정답 후보
        if tmp_sum >= B and min_height > tmp_sum:
            min_height = tmp_sum
        return
    #idx에 해당하는 요소를 부분집합에 포함하거나/안하거나
    tower(idx+1,tmp_sum + heights[idx])
    tower(idx + 1, tmp_sum)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    INF = float("inf")
    min_height = INF
    tower(0,0)
    print("#{} {}".format(tc,min_height-B))
