import sys
sys.stdin = open("2559_수열.txt", "r")

# N, K = map(int, input().split())
# tem = list(map(int, input().split()))
# sum_list = []
# for i in range(N-K+1):
#     sum_tem = 0
#     for j in range(i, i+K):
#         sum_tem += tem[j]
#     sum_list.append(sum_tem)
# print(max(sum_list))
#
#
# #################################
# 풀이 (누적합)
N, K = map(int, input().split())
data = list(map(int, input().split()))

max_t = -9999999999  # 최대값을 저장할 변수
for i in range(1, N):
    data[i] += data[i-1] # 누적
data.append(0)

for i in range(N-1, K-2, -1): # N-1부터 K-1까지 -1씩 떨어진다.
    data[i] -= data[i-K]
    if data[i] > max_t:
        max_t = data[i]

print(max_t)

##################################
# 두번째 풀이
N, K = map(int, input().split())
t = list(map(int, input().split()))
res = sum(t[:K])
max_t = res
for i in range(K, N):
    res += t[i]
    res -= t[i-K]
    if res > max_t:
        max_t = res

print(max_t)