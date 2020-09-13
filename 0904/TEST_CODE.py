# 멱집합 : 모든 부분집합
# 조합  : 특정 조건을 만족하는 부분집합
# 순열 : 요소들의 순서정렬
N = 3
arr = [6,5,3]
     #[0,0,0] 각 요소가
     # 부분집합에 포함되는지 표시하는 배열
selected = [0] * N

#idx 몇 번째 요소의 포함여부를 결정할지 표시하는 변수
def powerset(selected,idx,sum):             # idx는 부분집합 원소의 갯수
    if sum > 10:
        return

    if idx == N: #여기에 진입하는 횟수가 모든 부분집합의 경우의 수와 같다.
        #print(selected)
        for i in range(N):
            if selected[i] == 1:
                print(arr[i],end=" ")
        print()
        return
    #현재 상태에서 실행할 수 있는 모든 경우의 수 실행
    #현재요소 포함
    selected[idx] = 1
    powerset(selected,idx + 1,sum + arr[idx])

    # 현재요소 미포함
    selected[idx] = 0
    powerset(selected, idx + 1, sum)

    # for i in range(2):
    #     selected[idx] = i
    #     powerset(idx+1)



powerset(selected,0,0)
# 부분집합의 합이 5이하인 부분집합을 모두 출력하라