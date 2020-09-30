import sys
sys.stdin = open("2635_수이어가기.txt", "r")

N = int(input())
list_all = []
for i in range(1, 1+N):
    num_list = []
    num_list.append(N)
    num_list.append(i)
    idx = 0
    new_num = 0
    while new_num >= 0:
        new_num = num_list[idx]-num_list[idx+1]
        if new_num >= 0:
            num_list.append(new_num)
        idx += 1
    list_all.append(num_list)
max_len = 0
max_list = 0
for i in range(len(list_all)):
    if max_len < len(list_all[i]):
        max_len = len(list_all[i])
        max_list = list_all[i]
print(max_len)
for i in range(len(max_list)):
    print(max_list[i], end=" ")

#############################################
# 풀이
N = int(input())
max_l = -1
max_li = []
for i in range(1, 101):
    tmp = [N, i]
    while 1:
        next = tmp[-2]-tmp[-1]
        if next <0:
            if len(tmp) > max_l:
                max_l = len(tmp)
                max_li = tmp
            break
        else:
            tmp.append(next)
print(max_l)
print(*max_li)    # *쓰면 리스트없이 숫자만
