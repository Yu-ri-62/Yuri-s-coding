import sys
sys.stdin = open("전자카트.txt", "r")

def road(i, N):
    if sum(visited) == N:
        case.append(board[i][0])
        new_v = case[:]
        case_sum.append(sum(new_v))
        case.pop()

    else:
        for j in range(N):
            if visited[j] == 0 and board[i][j] != 0:
                case.append(board[i][j])
                visited[j] = 1
                road(j, N)
                visited[j] = 0
                case.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)
    visited[0] = 1
    case = []
    case_sum =[]
    road(0, N)
    print("#{} {}".format(tc, min(case_sum)))
