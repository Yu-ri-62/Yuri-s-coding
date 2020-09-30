import sys
sys.stdin = open("1244_스위치켜고끄기.txt", "r")

def one(number):
    # for i in range(2, N+1):
    while number <= N:
        if switch[number] == 1:
            switch[number] = 0
            number += num
        else:
            switch[number] = 1
            number += num
    return switch

def two(num):
    for i in range(1, N):
        if 0 <= num + i <= N and 0 <= num - i <= N and switch[num + i] == switch[num - i] :
            if switch[num + i] == 1 and switch[num - i] == 1:
                switch[num + i] = 0
                switch[num - i] = 0
            else:
                switch[num + i] = 1
                switch[num - i] = 1
        else:
            if switch[num] == 0:
                switch[num] = 1
                return switch
            else:
                switch[num] = 0
                return switch

N = int(input())
switch = [2] + list(map(int, input().split()))
T = int(input())
for tc in range(T):
    gen, num = map(int, input().split())
    if gen == 1:
        one(num)
    else:
        two(num)
for i in range(1,len(switch)):
    print(switch[i], end=" ")
    if not i % 20:
        print()

###########################################
# 풀이
import sys
sys.stdin = open('스위치.txt')
# 입력
T = int(input())
arr = list(map(int, input().split()))
C = int(input())
# 학생수 만큼
for i in range(C):
    # 학생 성별과 학생 받은 수
    a, b = map(int, input().split())
    # 남학생이면
    if a == 1:
        for j in range(b-1, len(arr), b):
            arr[j] = arr[j]^1
    # 여학생일때
    else:
        b = b - 1 # 인덱스 맞춰주기.
        arr[b] = arr[b] ^ 1
        # 회문처럼 하나씩 양 옆을 검사
        for j in range(1, min(len(arr)-b,b+1)):
            if arr[b-j] == arr[b+j]:
                arr[b-j] = arr[b-j]^1
                arr[b + j] = arr[b + j] ^ 1
            # 안 맞는 것이 있다면 바로!! 브레이크
            else:
                break
# 20줄씩 출력
print(arr[0], end=' ')
for i in range(1, len(arr)):
    if i%20 == 0 :
        print()
    print(arr[i], end=' ')