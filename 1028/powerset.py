#[1,2,3] N : 3 요소가 3개인 집합의 모든 부분집합
N = 3
arr = [1,2,3]
selected = [0] * N
def powerset(selected,idx):
    if idx == N:
        print(selected)
        return

    selected[idx] = 1
    powerset(selected,idx+1)
    selected[idx] = 0
    powerset(selected, idx + 1)

powerset(selected,0)