import sys
sys.stdin = open("최빈수구하기.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 테스트케이스 번호
    input()

    # 0~100점까지 세야하므로
    # 각각의 인덱스를 점수로 보고 값을 카운트한 개수로 본다.
    cnt = [0] * 101

    # 점수 입력
    score = list(map(int, input().split()))

    for i in score:
        cnt[i] += 1

    # ans = 0
    #
    # for i in range(101):
    #     if cnt[i] >= ans:
    #         ans = i

    # 최빈수 개수를 담아두었어요.
    ans = max(cnt)

    for i in range(100, -1, -1):
        if ans == cnt[i]:
            ans = i
            break

    print("#{} {}".format(tc, ans))