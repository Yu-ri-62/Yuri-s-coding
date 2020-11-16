import sys
sys.stdin = open("최대상금.txt", "r")

T = int(input())
for tc in range(1, T+1):
    number, N = input().split()
    N = int(N)

    number_list = []
    for i in range(len(number)):
        number_list.append([i, int(number[i])])

    # if N == 1:
    #     for n in range(N):
    #         for i in range(len(number_list)):
    #             for j in range(i, len(number_list)):
    #                 if number_list[i] < number_list[j]:
    #                     number_list[i], number_list[j] = number_list[j], number_list[i]
    # else:
    #     cnt = number_list.count(max(number_list))
    #     change = min(cnt, N)

    #print(number_list)
    number_list.reverse()
    print(number_list)
    for n in range(N):
        for i in range(len(number_list)//2):
            number_list[i], number_list[len(number_list)-i] = number_list[len(number_list)-i], number_list[i]
        print(number_list)

# arr = [(0, 3), (1, 2), (2, 8), (3, 8), (4, 8)]
# for len(arr)//2
# arr.sort()
# arr.sort(key=lambda x:x[1])
# print(arr)
