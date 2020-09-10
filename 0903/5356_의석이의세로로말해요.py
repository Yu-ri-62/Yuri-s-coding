import sys
sys.stdin = open("5356_의석이의세로로말해요.txt", "r")




# 풀이
T = int(input())
for tc in range(1, T+1):
    words = [0] * 5
    maxlen = 0 #가장 길이가 긴 단어의 길이만큼만 반복을 해보면된다.

    for i in range(5):
        words[i] = list(input())
        if len(words[i]) > maxlen:
            maxlen = len(words[i])

    print("#{}".format(tc), end=" ")
    for i in range(maxlen):
        for j in range(5):
            #인덱스 범위안에 들어왔을 때만 출력.
            # if len(words[j])  >i:
            #     print(words[j][i], end="")
            try:
                print(words[j][i], end="")
            except:
                pass
    print()