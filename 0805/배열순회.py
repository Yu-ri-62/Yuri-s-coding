arr = [ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

N = len(arr)  # 행의 길이
M = len(arr)  # 열의 길이
# 행우선
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j], end= " ")
#     print()
# print()

# 열우선
for j in range(M):  #열
    for i in range(N):  #행
        print(arr[i][j], end= " ")
    print()
print()