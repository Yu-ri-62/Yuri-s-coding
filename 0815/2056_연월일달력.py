import sys
sys.stdin = open("2056_연월일달력.txt", "r")

T = int(input())
for tc in range(1, T+1):
    day = input()
    year = int(day[0:4])
    month = int(day[4:6])
    date = int(day[6:8])
    if 1<= month <= 12:
        if month == 2:
            if date <= 28:
                print('#%d' %tc, ' ', day[0:4],'/', day[4:6], '/', day[6:8], sep="")
            else:
                print('#%d' %tc, '-1')
        elif month == 4 or 6 or 9 or 11:
            if date <= 30:
                print('#%d' %tc, ' ', day[0:4],'/', day[4:6], '/', day[6:8], sep="")
            else:
                print('#%d' %tc, '-1')
        elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if date <=31:
                print('#%d' %tc, ' ', day[0:4],'/', day[4:6], '/', day[6:8], sep="")
            else:
                print('#%d' %tc, '-1')
    else:
        print('#%d' %tc, '-1')



