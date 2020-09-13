import sys
sys.stdin = open("4613_러시아국기같은깃발.txt", "r")

#러시아 국기 같은 깃발
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [input() for _ in range(N)]
    INF = float('inf') #많이 큰 수를 표현할 때 사용
    min_cnt = INF   #바뀌는 영역의 최소값을 저장하기 위한 변수
    #흰색 , 파란색, 빨간색 영역 구분하기
    #흰색, 파란색 영역이 끝나는 인덱스로 구분하자!
    # 흰색이 끝날 수 있는 인덱스 : 0~ N-2-1
    # 파란색이 끝날 수 있는 인덱스 : 흰색영역 +1 ~ N-1-1
    # 빨간색 영역 :파란색 영역 +1~ N-1
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            # 여기서 세개의 영역으로 구분할 수 있음
            # 0~i, i+1~j, j+1~끝
            cnt = 0
            # 흰색 영역 순회하면서 바꿔야할 개수 세기
            for w in range(0,i+1):  #i가 흰색영역의 끝이니 i를 포함해야함
                for k in range(M):
                    if flag[w][k] != 'W':
                        cnt += 1
            # 파란 영역 순회하면서 바꿔야할 개수 세기
            for b in range(i+1,j+1):
                for k in range(M):
                    if flag[b][k] != 'B':
                        cnt += 1
            # 빨간 영역 순회하면서 바꿔야할 개수 세기
            for r in range(j+1,N):
                for k in range(M):
                    if flag[r][k] != 'R':
                        cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt
    print("#{} {}".format(tc,min_cnt))


#################################################################

arr = [1,2,3,4]
N = 4
selected = [0] * N
T = 2 #원하는 조합의 요소 개수
# selected : 어떤 요소가 선택되었는지 표시하는 배열
# idx : 요소의 인덱스
# cnt : 선택된 요소의 개수
def comb(selected,idx,cnt):
    if cnt == T:
        # 내가 원하는 개수만큼의 요소를 선택했음
        # print(selected)
        #내가 원하는 조합을 만들었으니....
        #원하는 계산은 여기에서 하시면 됩니다....
        #깃발을 어디서 나눌것인지에 대한 인덱스 변수
        #인덱스 2개 받아와야함
        a = -1
        b = -1
        for i in range(N):
            if selected[i] == 1:
                if a == -1:
                    a = i
                else:
                    b = i

        for i in range(0,a+1): #흰색
            pass
        for i in range(a+1,b+1): # 파란색
            pass
        for i in range(b+1,N): # 빨간색
            pass








        return
    if idx >= N-1:
        return

    #요소를 선택하거나/ 선택하지 않거나 모든 경우의 수 감안

    selected[idx] = 1   #idx에 해당하는 요소를 포함
    comb(selected,idx+1,cnt+1)
    selected[idx] = 0
    comb(selected,idx+1,cnt)
    return  # 내가 할 수 있는 모든 경우의 수 다 봤으니 내 턴을 종료한다.

comb(selected,0,0)