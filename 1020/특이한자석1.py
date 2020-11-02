import sys
sys.stdin = open("특이한자석.txt", "r")

T = int(input())
for test_case in range(1, 1 + T):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        idx, rot = map(int, input().split())
        idx -= 1  # 0 ~ 3번 톱니
        move = [(idx, rot)]  # 돌릴 톱니

        # 왼쪽 톱니 확인
        temp = rot
        for i in range(idx - 1, -1, -1):
            if mag[i][2] != mag[i + 1][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 오른쪽 톱니 확인
        temp = rot
        for i in range(idx + 1, 4):
            if mag[i][6] != mag[i - 1][2]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 톱니 돌림
        for idx, rot in move:
            if rot == 1:
                mag[idx] = [mag[idx].pop()] + mag[idx]
            elif rot == -1:
                mag[idx].append(mag[idx].pop(0))

    # 결과 계산
    result = 0
    for i in range(4):
        result += mag[i][0] * 2**i

    print('#{} {}'.format(test_case, result))