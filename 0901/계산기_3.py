import sys
sys.stdin = open("계산기_3.txt", "r")

T = 10
for tc in range(T):
    case = int(input())
    str_list = list(input())
    icp = {'(':3, '*':2, '+':1}
    isp = {'*':2, '+':1, '(':0}
    stack = []
    cal_list = []
    for i in range(len(str_list)):
        if str_list[i] != '(' and str_list[i] != ')' and str_list[i] != '*' and str_list[i] != '+':    # 숫자일 때
            cal_list.append(str_list[i])
        else:                                                                                          # 연산자일 때
            if len(stack) == 0:                                                                        # 스택에 아무것도 없을 때
                stack.append(str_list[i])
            else:                                                                                      # 스택에 연산자가 있을 때
                if isp[stack(-1)] < icp[str_list[i]]:                                                  # 스택에 있는 연산자가 들어올 연산자 보다 우선순위가 낮으면

