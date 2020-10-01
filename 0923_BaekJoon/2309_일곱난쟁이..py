import sys
sys.stdin = open("2309_일곱난쟁이.txt", "r")

tall = [int(input()) for _ in range(9)]
nan = 0
for i in range(len(tall)):
    for j in range(len(tall)):
        if i != j:
            nan = sum(tall)-tall[i]-tall[j]
            if nan == 100:
                a = tall[i]
                b = tall[j]
                tall.remove(a)
                tall.remove(b)
                break
    if nan == 100:
        break
tall.sort()
for i in range(len(tall)):
    print(tall[i])
