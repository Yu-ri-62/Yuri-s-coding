import sys
sys.stdin = open("5201_컨테이너운반.txt", "r")

def truck():
    for j in range(len(W) - 1, -1, -1):
        for i in range(len(T)-1, -1, -1):
            if T[i] >= W[j]:
                result.append(W[j])
                W.pop()
                T.pop()
                break
    return result

def container():
    for i in range(len(T)-1, -1, -1):
        for j in range(len(W)-1, -1, -1):
            if T[i] >= W[j]:
                result.append(W[j])
                break
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N = 컨테이너 수 , M = 트럭 수
    W = list(map(int, input().split()))  # W = 화물의 무게
    T = list(map(int, input().split()))  # T = 트럭의 적재 용량
    W.sort()
    T.sort()
    result = []
    if len(W) > len(T):
        container()
    else:
        truck()
    print("#{} {}".format(tc, sum(result)))