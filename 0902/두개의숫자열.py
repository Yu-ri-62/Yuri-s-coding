import sys
sys.stdin = open("두개의숫자열.txt", "r")

def calc(long, short):
    max_value = -987654321

    # 긴거에서 짧은거 빼기
    for i in range(len(long) - len(short) + 1):
        result = 0
        for j in range(len(short)):
            result += long[i + j] * short[j]

        if max_value < result:
            max_value = result

    return max_value


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 리스트 두개 입력
    numsA = list(map(int, input().split()))
    numsB = list(map(int, input().split()))

    if len(numsA) > len(numsB):
        ans = calc(numsA, numsB)
    else:
        ans = calc(numsB, numsA)

    print("#{} {}".format(tc, ans))

