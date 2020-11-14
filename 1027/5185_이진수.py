import sys
sys.stdin = open("5185_이진수.txt", "r")

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

T = int(input())
b_list = []
for tc in range(1, T+1):
    N, hex = list(input().split())
    for i in range(len(hex)):
        if hex[i] in num:
            b_list.append(int(hex[i]))
        else:
            b_list.append(ord(hex[i])-55)
    #print(b_list)

    binary = []
    for i in range(len(b_list)):
        case = b_list.pop()
        cnt = 0
        while case // 2 >= 1:
            binary.append(case % 2)
            cnt += 1
            case = case//2
        binary.append(case)
        cnt += 1
        if cnt < 4:
            for j in range(4-cnt):
                binary.append(0)
    #print(binary)
    new_binary = ''
    for i in range(len(binary)-1, -1, -1):
        new_binary += str(binary[i])
    print("#{} {}".format(tc, new_binary))
