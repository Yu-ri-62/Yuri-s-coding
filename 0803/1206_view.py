import sys
sys.stdin = open("1206_view.txt", "r")

T = 10
for tc in range(T+1):
    L = int(input())
    building = list(map(int, input().split()))
    sight = 0
    for i in range(2, L-2):
        left = 0
        left_view = 0
        right = 0
        right_view = 0
        if building[i-1]> building[i-2]:
            left = building[i-1]
        else:
            left = building[i-2]
        left_view = building[i]-left

        if building[i+1]> building[i+2]:
            right = building[i+1]
        else:
            right = building[i+2]
        right_view = building[i]-right
        if left_view <= 0 or right_view <= 0:
            continue

        if left_view > right_view:
            sight += right_view
        else:
            sight += left_view
    print("#{} {}".format(tc, sight))