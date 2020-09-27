# 인덱스를 이용해서 숫자 출현 횟수 체크하기
#만약에 숫자가 1~9까지 주어진다면
#arr = [0] * 10  # 인덱스는 0~9번
# 한 칸 더 만들면 마음이 편안하다....ㅎㅎ
#[0][1][2][3][4][5][6][7][8][9]
#
# import sys
# sys.stdin = open("1974_스도쿠.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = []
#     for num in range(9):
#         numbers = list(map(int, input().split()))
#         arr.append(numbers)
#
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] == arr[j]:
#                 break
#         if arr[i] == arr[j]:
#             break
#
#
#     for k in range(len(arr[0])):
#         for l in range(len(arr)):
#             if arr[k] == arr[l]:
#                 break
#         if arr[k] == arr[l]:
#             break
#
#     for m in range(0, 9, 3):
#         for n in range(0, 9, 3):
#             for o in range(m, m+3):
#                 for p in range(n, n+3):
#                     arr[o][p]


#############################################################
import sys
sys.stdin = open("1974_스도쿠.txt", "r")
T = int(input())

for tc in range(1, T+1):
    arr = []
    arr_list = []

    compare_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1
    for num in range(9):
        numbers = list(map(int, input().split()))
        arr.append(numbers)
    arr_1 = copy.deepcopy(arr)
    for i in arr_1:
        arr_list = sorted(i)
        if compare_list != arr_list:
            result = 0
    arr_2 = copy.deepcopy(arr)
    for i in range(len(arr)):
        arr_list1 = []
        for j in range(len(arr)):
            arr_list1.append(arr_2[j][i])

        arr_list1.sort()
        if compare_list != arr_list1:
            result = 0
    arr_3 = copy.deepcopy(arr)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr_list2 = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    arr_list2.append(arr_3[k][l])
                    arr_list2.sort()

            if compare_list != arr_list2:
                result = 0
    print("#%d" % tc, result)

########################################################

def check_sudoku(sudoku): # 스도쿠라면 True, 아니라면 False
    # 모든 행검사
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            if check[sudoku[i][j]] == 0:
                check[sudoku[i][j]] = 1
            else: #숫자 중복 발생 >> 스도쿠 아님
                return 0
    # 모든 열검사
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            if check[sudoku[j][i]] == 0:
                check[sudoku[j][i]] = 1
            else:  # 숫자 중복 발생 >> 스도쿠 아님
                return 0
    # 3*3 행렬 9개 검사
    for i in range(0,9,3):
       for j in range(0,9,3):
           check = [0] * 10
           for r in range(i,i+3):
               for c in range(j,j+3):
                   if check[sudoku[r][c]] == 0:
                       check[sudoku[r][c]] = 1
                   else:
                       return 0
    return 1


#스도쿠검증
import sys
sys.stdin = open("input.txt","r")
T = int(input())
for tc in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    #1~9까지 숫자가 한 번씩 나오는지 검사
    # check 배열 : 숫자가 한 번씩 나오는지 검사하는 배열
    # 0  1  2  3  4  5  6  7  8  9
    #[0][0][0][1][0][0][0][1][0][0]
    result = check_sudoku(sudoku)
    print("#{} {}".format(tc,result))


