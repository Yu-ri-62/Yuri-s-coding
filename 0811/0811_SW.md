## SW Expert Academy

### 1545_거꾸로 출력

```python
import sys
sys.stdin = open("1545_거꾸로출력.txt", "r")

T = int(input())            # 숫자를 int로 받는다.
for i in range(T,-1,-1):    # T부터 0까지 역순으로
    print(i, end=' ')       # 한 칸씩 띄어서 출력
```



### 1936_1대1가위바위보

```python
A, B = map(int, input().split())    # 입력되는 두 숫자를 int형으로 변환한다.
if A > B:                           # A가 B보다 크면서
    if A == 3 and B == 1:           # A가 3일 때,
        print('B')                  # B가 출력됨  
    print('A')                      # A가 크면 A가 출력
else:                               # B가 A보다 크면서
    if B == 3 and A == 1:           # B가 3일 때,
        print('A')                  # A가 출력됨.
    print('B')                      # B가 크면 B가 출력
```



### 2019_더블더블

```python
T = int(input())                # 들어오는 값을 int로 변환
for i in range(T+1):            # 범위 0부터 T까지 
    if i == 0:                  # i가 0일 때
        print(1, end=" ")       # 1출력
    else:                       # i가 0이 아닐 때
        print(2**i, end=" ")    # i**2
```

