import sys
sys.stdin = open("특이한자석.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    rota = [list(map(int, input().split())) for _ in range(K)]
    for i in range(K):
        a = rota[i][0]-1
        stack = []
        # stack.append(a)
        while 0 <= a+1 <= 3 or 0 <= a-1 <= 3:
            if 0 <= a+1 <= 3:
                if mag[a][2] != mag[a+1][6]:
                    stack.append(a+1)
                else:
                    break
                a += 1
            else:
                a = rota[i][0] - 1
                break

        while 0 <= a-1 <= 3:
            if 0 <= a-1 <= 3:
                if mag[a][6] != mag[a-1][2]:
                    stack.append(a-1)
                else:
                    break
                a -= 1
            else:
                break

        if rota[i][1] == 1:
            b = rota[i][0]-1
            app = mag[b].pop()  # 마지막을
            mag[b].insert(0, app)  # 앞으로
            while stack:
                c = stack.pop(0)
                if c == b+1 or c == b-1:
                    app_1 = mag[c].pop(0) # 맨 앞을
                    mag[c].append(app_1)  # 뒤로
                if c == b+2 or c == b-2:
                    app_1 = mag[c].pop()
                    mag[c].insert(0, app_1)
                if c == b+3 or c == b-3:
                    app_1 = mag[c].pop(0)  # 맨 앞을
                    mag[c].append(app_1)  #
        elif rota[i][1] == -1:
            b = rota[i][0]-1
            app = mag[b].pop(0)
            mag[b].append(app)
            while stack:
                c = stack.pop(0)
                if c == b + 1 or c == b - 1:
                    app_1 = mag[c].pop()
                    mag[c].insert(0, app_1)
                if c == b+2 or c == b-2:
                    app_1 = mag[c].pop(0)  # 맨 앞을
                    mag[c].append(app_1)
    sum_num = 0
    for i in range(4):
        if mag[i][0] == 1:
            sum_num += 2**i
    print(sum_num)