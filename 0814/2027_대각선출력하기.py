import sys
sys.stdin = open("2027_대각선출력하기.txt", "r")

number = 0
for i in range(5):
    for j in range(5):
        if j == number:
            print('#', end='')
        else:
            print('+', end='')
    print()
    number += 1
