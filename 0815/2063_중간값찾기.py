import sys
sys.stdin = open("2063_중간값찾기.txt", "r")

T = int(input())
number_list = list(map(int, input().split( )))
for i in range(len(number_list)-1):
    for j in range(len(number_list)-1):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
print(number_list[T//2])