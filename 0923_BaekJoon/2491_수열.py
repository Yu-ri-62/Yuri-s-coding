import sys
sys.stdin = open("2491_수열.txt", "r")

N = int(input())
num_list = list(map(int, input().split()))
max_cnt = 0
for i in range(N-1):
    cnt = 1
    if max_cnt <= N-(i+1):
        while i < N-1 and num_list[i] <= num_list[i+1]:
            cnt += 1
            i += 1
        if cnt > max_cnt:
            max_cnt = cnt
for i in range(N-1):
    cnt = 1
    if max_cnt <= N-(i+1):
        while i < N-1 and num_list[i] >= num_list[i+1]:
            cnt += 1
            i += 1
        if cnt > max_cnt:
            max_cnt = cnt
print(max_cnt)

###############################################
# 풀이
N = int(input())

li = list(map(int, input().split()))

cnt_p = 1   #  연속증가 길이
cnt_m = 1   #  연속감소 길이
max_cnt = 1   #  연속증가 or 연속감소 최대 길이

for i in range(1, N):
    if li[i] > li[i-1]:       # 증가
        cnt_p += 1
        cnt_m = 1
    elif li[i] < li[i-1]:     # 감소
        cnt_m += 1
        cnt_p = 1
    elif li[i] == li[i-1]:    # 같을때
        cnt_p += 1
        cnt_m += 1

    if max_cnt < cnt_p:
        max_cnt = cnt_p
    elif max_cnt < cnt_m:
        max_cnt = cnt_m
print(max_cnt)
