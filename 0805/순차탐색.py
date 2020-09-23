# 정렬되지않은
def seq_search(a, n, k):
    i = 0
    while i < n and a[i] != k:   # arr길이 안에서 K를 찾을 때 까지
        i += 1
    if i < n:
        return i
    else:
        return -1   # arr안에 없으면 -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 23
print(seq_search(arr, len(arr), key))

# 정렬되어있는
def seq_search(a, n, k):
    i = 0
    while i < n and a[i] < k:
        i += 1
    if i < n and a[i] ==key:
        return i
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 17, 18, 19]
key = 17
print(seq_search(arr, len(arr), key))
