pattern = [[0,0,1,1,0,1],
           [0,1,0,0,1,1],
           [1,1,1,0,1,1],
           [1,1,0,0,0,1],
           [1,0,0,0,1,1],
           [1,1,0,1,1,1],
           [0,0,1,0,1,1],
           [1,1,1,1,0,1],
           [0,1,1,0,0,1],
           [1,0,1,1,1,1]]

def hex_to_decimal(c):
    num = ord(c)
     # 숫자
    if 48 <= num <= 57:
        return num - 48
    elif 65 <= num <=70:
        return num - ord('A') + 10

def decimal_to_binary(n):   # 0~15
    binary = [0] * 4    # 0~15까지는 4개의 비트로 처리가능
    idx = 3
    while n > 0:
        # n을 2로 나누어서 나머지를 계속 저장
        binary[idx] = n % 2
        idx -= 1
        n = n//2
    return binary

# print(decimal_to_binary(15))
#  0000000 1   01
str = "0DEC"
result = list()
for i in range(len(str)):
    number = hex_to_decimal(str[i])
    result += decimal_to_binary(number)

for i in range(len(result)):
    tmp = result[i:i+6]
    if tmp in pattern:
        for j in range(i,len(result),6):
            password = result[j:j+6]
            if len(password ) == 6:
                print(pattern.index(password),end=" ")
        break   #바깥쪽 반복문 종료