import sys
sys.stdin = open("5177_이진힙.txt", "r")

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2

    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2

def sum_node(node):
    global total
    parent = node // 2
    if heap[parent] > 0:
        total += heap[parent]
        sum_node(parent)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    heap = [0]*(N+1)
    heapcount = 0
    total = 0
    for i in range(N):
        heappush(num_list[i])

    sum_node(N)
    print("#{} {}".format(tc, total))

##################################################
# 풀이

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0]*(N+1)
    hsize = 0


def push(item):
    global hsize
    hsize += 1
    H[hsize] = item
    c = hsize
    p = hsize//2
    while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c//2

# 함수를 사용하지 않고
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0]*(N+1)
    hsize = 0

    for val in arr:
        hsize += 1
        H[hsize] = val
        c = hsize
        p = hsize // 2

        while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
    ans = 0
    v = N//2
    while v:
        ans += H[v]
        v = v//2
    print(ans)

# heapq 사용
from heapq import heapify

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heapify(arr)
    v = (N-1)      # heapq는 root가 0으로 시작하기 때문에
