import sys
sys.stdin = open("2058_자릿수더하기.txt", "r")

T = list((input()))
list_sum = 0
for i in range(len(T)):
    list_sum += int(T[i])
print(list_sum)