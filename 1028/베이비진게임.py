import sys
sys.stdin = open("베이비진게임.txt", "r")


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    player_1 = [0]*10
    player_2 = [0]*10

    result = 0
    for i in range(len(card)):
        if i % 2 == 0:
            player_1[card[i]] += 1
            if 3 in player_1:
                result = 1
                break
            cnt_1 = 0
            for j in range(len(player_1)):
                if player_1[j] >= 1:
                    cnt_1 += 1
                    if cnt_1 == 3:
                        result = 1
                        break
                else:
                    cnt_1 = 0

        else:
            if result == 0:
                player_2[card[i]] += 1
                if 3 in player_2:
                    result = 2
                    break
                cnt_2 = 0
                for j in range(len(player_2)):
                    if player_2[j] >= 1:
                        cnt_2 += 1
                        if cnt_2 == 3:
                            result = 2
                            break
                    else:
                        cnt_2 = 0
    print("#{} {}".format(tc, result))


######################################
def check(arr):# arr이 run 이나 triplet 을 포함하면 return True, 아니면 False
    #런인지 검사 arr[i] == 1 and arr[i+1] == 1 and arr[i+2] ==1
    #triplet인지 검사
    for i in range(len(arr)):
        if i < len(arr)-2  and arr[i] > 0:
            if arr[i+1] > 0 and arr[i+2] > 0:
                return True
        if arr[i] == 3:
            return True
    return False

T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))

    p1 = [0] * 10   #각 플레이어가 어떤 카드를 몇 장 받았는지 저장하는 배열
    p2 = [0] * 10
    for i in range(len(cards)):
        if i % 2 == 0:
            p1[cards[i]] += 1
        else:
            p2[cards[i]] += 1
        # 카드를 받을 때마다, run이나 triplet 이 있는지 검사
        if check(p1):
            print("#{} 1".format(tc))
            break
        if check(p2):
            print("#{} 2".format(tc))
            break
    else:
        print("#{} 0".format(tc))