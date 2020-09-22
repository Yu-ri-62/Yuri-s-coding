
#상자로 채워진 방이 있다
#방을 오른쪽으로 90도 회전시켰을때
#낙차가 가장 큰 상자의 낙차를 구하여라

#낙차를 구하는 방법 : 원래모양에서 오른쪽에 있는 상자의 높이가 현재대상보다 작거나 상자가 쌓여있지 않으면 낙차를 증가시킨다.
#모든 열의 낙차를 구하고, 그 중에서 가장 큰 낙차를 반환(출력)한다.

#하나의 열의 낙차부터 구하기
#step 1. 가장 왼쪽에 있는 열(0번 열)의 낙차 구하기

#주석처리 ctrl + '/'
# target = boxes[0]
# count = 0
# for i in range(1, len(boxes)): #1번열부터 끝까지 순회
#     #target 보다 작은 값을 가지는 열의 수를 계산
#     if boxes[i] < target :
#         count += 1
#
# print(count)

#step 2. 모든의 낙차를 구하고, 최고 낙차 구하기
#max나 min값을 저장하는 변수를 선언 할때는 분명한 이유가 필요
#
boxes = [7, 4, 2, 0, 0, 6, 0, 7, 0]


max_count = 0 #0으로 초기화
for j in range(0, len(boxes)):
    target = boxes[j]
    count = 0
    for i in range(j+1, len(boxes)): #1번열부터 끝까지 순회
        #target 보다 작은 값을 가지는 열의 수를 계산
         if boxes[i] < target :
            count += 1

#print(count)
    if count > max_count:
        max_count = count

print(max_count)
#반복문 돌때마다, count의 값을 비교를 해서 더 큰 값을 남긴다.