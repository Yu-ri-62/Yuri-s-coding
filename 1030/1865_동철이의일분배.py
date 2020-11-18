import sys
sys.stdin = open("1865_동철이의일분배.txt", "r")


#모든 경우의 수에서, 불가능한 경우를 제외하자!
# 결국에 업무의 순서>> 업무의 순서가 필요한게 아니라,
# 직원들이 각 일을 했을 때 성공확률이 최대가 되면됨
# 0.xx * 0.xxx * 0.xxx   * 1.0  * 100 :
# 성공확률을 곱할 때 마다 확률은 줄어듬, 우리는 최대값을 찾아야 함
# 중간 결과가 이전의 최대 값보다 작으면, 더 이상 계산 할 필요가 없음
# rate : 중간 계산 확률
# used : 해당 업무가 이미 할당된 업무인지 표시하기 위한 배열
def solve(used,idx,rate):
    global max_rate
    if rate <= max_rate: #중간 계산 결과가 이전 최대값 보다 작으면,
        return
    if idx >= N:    #마지막 직원 까지 모두 업무할당 완료
        if rate > max_rate:
            max_rate = rate
        return

    for i in range(N):
        if used[i]: continue
        used[i] = 1 # i번째 업무가 배정되었음을 표시
        solve(used,idx+1,rate * arr[idx][i])
        used[i] = 0 #원래대로 돌려놓기


for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_rate = 0
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    used = [0] * N
    rate = 1
    solve(used,0,rate)
    print("#%d %0.6f" % (tc,round(max_rate*100,6)))
