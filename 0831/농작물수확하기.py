import sys
sys.stdin = open("농작물수확하기.txt", "r")

###############################################
# 중앙을 기준으로 좌/우 순회 범위를 정해주기
# 행이 늘어나면, 좌우 영역이 1씩 증가하다가
# 중앙선을 넘어서면 다시 좌우 영역이 1씩 감소한다.

# 입력받고

# 큰 방복문 N번 순회

# 그 안에서 왼쪽 범위부터 오른쪽 범위까지 돌면서 값을 더해주자.
# 이 때 행이 중앙을 넘지 않았다면 좌우가 증가
# 중앙을 넘었다면 좌우가 감소

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]  # 2차원 배열로 입력받기

    step = 0                                            # 행이 늘어나면서 한 칸씩 늘리기 위해 변수 설정
    mid = N//2                                          # 행 중에서 중간에 있는 행
    ans = 0

    for i in range(N):
        # 행을 순회 하면서 행마다 열 인덱스 설정
        for j in range(mid-step, mid+step+1):          # mid-step 부터 mid+step까지 범위
            ans += farm[i][j]                          # i가 0, 1, 2...일때 중앙에 위치한 값

        if i < mid:                                    # 중간 행 까지는 step이 늘어난다.
            step += 1
        else:                                          # 중간 행을 지나면 step은 감소한다.
            step -= 1
    print("#{} {}".format(tc, ans))


################################################
# 중앙을 기준으로 위아래가 좌우 범위의 중복이 발생하므로 절반만 돌고도 구할 수 있다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]  # 2차원 배열로 입력받기

    row = N//2                                          # 행의 반 까지
    ans = 0

    for j in range(N):
        ans += farm[row][j]                             # 행의 중간은 j가 N만큼 있고
    for i in range(1, N//2+1):                          # 행의 중간을 제외한 감소 or 증가 할 만큼의 범위
        st = 0 + i                                      
        ed = N-1 -i
        for j in range(st, ed+1):                        #
            ans += farm[row+i][j] + farm[row-i][j]
    print("#{} {}".format(tc, ans))