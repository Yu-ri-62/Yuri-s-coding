import sys
sys.stdin = open("정식이의은행업무.txt", "r")

T = int(input())
for tc in range(1, T+1):
    two = list(map(int, input()))
    three = list(map(int, input()))
    two_list = []
    three_list = []

    for i in range(len(two)):
        if two[i] == 0:
            two[i] = 1
            sum_two = 0
            for j in range(len(two)):
                if two[j] == 1:
                    sum_two += 2**(len(two)-j-1)
            two_list.append(sum_two)
            two[i] = 0
        else:
            two[i] = 0
            sum_two = 0
            for j in range(len(two)):
                if two[j] == 1:
                    sum_two += 2 ** (len(two) -j-1)
            two_list.append(sum_two)
            two[i] = 1
    #print(two_list)

    for i in range(len(three)):
        if three[i] == 2:
            three[i] = 1
            sum_three = 0
            for j in range(len(three)):
                sum_three += three[j] * (3 ** (len(three) - j - 1))
            three_list.append(sum_three)
            three[i] = 0
            sum_three = 0
            for j in range(len(three)):
                sum_three += three[j] * (3 ** (len(three) - j - 1))
            three_list.append(sum_three)
            three[i] = 2
        elif three[i] == 1:
            three[i] = 2
            sum_three = 0
            for j in range(len(three)):
                sum_three += three[j] * (3 ** (len(three) - j - 1))
            three_list.append(sum_three)
            three[i] = 0
            sum_three = 0
            for j in range(len(three)):
                sum_three += three[j] * (3 ** (len(three) - j - 1))
            three_list.append(sum_three)
            three[i] = 1
        else:
            three[i] = 2
            sum_three = 0
            for j in range(len(three)):
                sum_three += three[j] * (3 ** (len(three) - j - 1))
            three_list.append(sum_three)
            three[i] = 1
            sum_three = 0
            for j in range(len(three)):
                sum_three += three[j] * (3 ** (len(three) - j - 1))
            three_list.append(sum_three)
            three[i] = 0
    #print(three_list)
    for i in range(len(two_list)):
        if two_list[i] in three_list:
            print("#{} {}".format(tc, two_list[i]))
            break
