import sys
sys.stdin = open("4874_Forth.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str_list = list(input().split())
    stack = []
    result = 0
    result1 = 0
    for i in range(len(str_list)):
        if str_list[i] != '+' and str_list[i] != '-' and str_list[i] != '*' and str_list[i] != '/' and str_list[i] != '.':   # 숫자일 때
            stack.append(str_list[i])                                                              # 스택에 쌓기
        else:                                                                                      # 연산자일 때
            if len(stack) >= 2:                                                                 # 스택의 길이가 2이상이면
                tmp1 = stack.pop()                                                                 # 두번 팝 하기
                tmp2 = stack.pop()
                if str_list[i] == '+':                                                             # 연산자에 따라 연산하기
                    result = int(tmp2)+int(tmp1)
                    stack.append(result)
                elif str_list[i] == '-':
                    result = int(tmp2)-int(tmp1)
                    stack.append(result)
                elif str_list[i] == '/':
                    result = int(tmp2)//int(tmp1)                                                  # 무조건 나누어떨어져야 하기 때문데
                    stack.append(result)
                elif str_list[i] == '*':
                    result = int(tmp2)*int(tmp1)
                    stack.append(result)
                else:
                    print("#{} {}".format(tc, 'error'))
                    break
            else:                                                                                       # stack 길이가 2보다 작을 때
                if str_list[i] == '.':                                                                  # . 일때
                    result1 = stack.pop()
                    print("#{} {}".format(tc, result1))
                    break
                else:
                    print("#{} {}".format(tc, 'error'))
                    break
