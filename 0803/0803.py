import sys
sys.stdin = open('input1.txt','r')
t = 10
for j in range(t):
    n = int(input())
    #print(n)
    boxes = list(map(int, input().split()))
    #print(boxes)
    house = 0
    for i in range(2, len(boxes) - 2):
        if boxes[i] > max(boxes[i + 1], boxes[i + 2]):
            right = boxes[i] - max(boxes[i + 1], boxes[i + 2])
        else:
            right = 0
        if boxes[i] > max(boxes[i - 1], boxes[i - 2]):
            left = boxes[i] - max(boxes[i - 1], boxes[i - 2])
        else:
            right = 0
        house += min(right, left)
    print('#{} {}'.format(j+1, house))
