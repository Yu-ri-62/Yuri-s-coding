#"0000000111100000011000000111100110000110000111100111100111111001100111"

number = list(input())
num_list = []
cal = []

for x in range(10):
    for i in range(7):
        a = number.pop(0)
        num_list.append(a)

    num_list.reverse()
    sum_num = 0
    for i in range(len(num_list)):
        b = int(num_list[i])
        if b == 1:
            sum_num += 2**(i)
    cal.append(sum_num)
    num_list = []
print(cal)


#############################################
#풀이
# 이진수 문자열을 입력받아서  10진수 숫자로 변경하는 문제
# 0000000111100000011000000111100110000110000111100111100111111001100111
# 2진수 >>> 10진수로 변경
# 각 비트에 해당하는 2^n의 숫자를 다 더해주면 됨
# 4개 비트 2진수 :    [0,1,1,0]   >>> [2^3,2^2,2^1,2^0]
# 0110을 10진수로 변환  : 2^2 + 2^1 : 5
arr = list(map(int,input()))
for i in range(0,len(arr),7):
    # 111100 >>> 2^6 + 2^5 + 2^4 + 2^3 + 0 + 0
    cnt = 6
    num = 0
    for j in range(i,i+7):
        if arr[j] == 1:
            num += (2**cnt)
        cnt -= 1
    print(num, end= " ")