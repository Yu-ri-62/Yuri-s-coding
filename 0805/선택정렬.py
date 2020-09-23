def selectionSort(a):
    # i : 0 ~len(n)-1
    for i in range(len(a)-1):  # 0, 1, 2, 3
        #최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

arr = [64, 25, 10, 22, 11]
selectionSort(arr)
print(arr)
#----------------------------------------------------------------------
#
# def selectionSort(a, k):
#     # i : 0 ~len(n)-1
#     for i in range(k):  # 0, 1, 2, 3
#         #최소값 찾기
#         min = i
#         for j in range(i+1, len(a)):
#             if a[min] > a[j]:
#                 min = j
#         a[i], a[min] = a[min], a[i]
#     return a[k-1]
#
# def selectionSort(a):
#     for i in range(len(a)-1):
#
# arr = [64, 25, 10, 22, 11]
# selectionSort(arr)
# print(arr)
# selection(arr, 3)