# 10개의 정수 집합에 대한 모든 부분집합 중 원소의 합이 0이 되는 부분집합을 모두 출력하시오.

N = 10
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# selected = [0] * N
selected = list()
def powerset(selected,idx):
    if idx == N:
        if sum(selected) == 0:
            print(*selected,sep=",")
        return

    selected.append(arr[idx])
    powerset(selected,idx+1)

    selected.pop()
    powerset(selected, idx + 1)

powerset(selected,0)