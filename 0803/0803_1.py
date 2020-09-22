import sys
sys.stdin = open('input1.txt','r')
for j in range(10):
    n = int(input())
    #print(n)
    boxes = list(map(int, input().split()))
    #print(boxes)
    sum_house = 0
    for i in range(2, len(boxes) - 2):
        if boxes[i] > max(boxes[i + 1], boxes[i + 2]) and boxes[i] > max(boxes[i - 1], boxes[i - 2]):
            house = max(max(boxes[i + 1], boxes[i + 2]), max(boxes[i - 1], boxes[i - 2]))
            sum_house += boxes[i] - house
    print('#{} {}'.format(j+1, sum_house))