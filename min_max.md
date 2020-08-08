## SW Expert Academy

### 4828 min_max

```
import sys
sys.stdin = open("min_max.txt", "r")

T = int(input())
for tc in range(1,  T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    min = numbers[0]
    max = numbers[0]

    for i in range(N):
        if max < numbers[i]:
            max = numbers[i]
        if min > numbers[i]:
            min = numbers[i]

    print("#%d" % tc, max-min)
```



###  4831 전기버스

```
import sys
sys.stdin = open("전기버스.txt", "r")

T = int(input())
total = 0
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    car = 0
    count = 0
    for i in range(M-1):
        if station[i+1] - station[i] > K:
            car = N


    while(car < N):
        car += K
        if car >= N:
            break
        while (car not in station):
            car -= 1
        count += 1
    print("#%d" % tc, count)
```



### 4834 숫자카드

```
import sys
sys.stdin = open("숫자카드.txt", "r")

def count(number_list, n):
    cnt = 0
    for number in number_list:
        if number == n:
            cnt += 1
    return cnt

T = int(input())
li = []
cnt = 0
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    M = 0
    res = 0
    for card in cards:
        if M < count(cards, card):
            M = count(cards, card)
            res = card
        elif M == count(cards, card):
            if res < card:
                res = card

    print("#%d %d %d" % (tc, res, M))
```





### 4835 구간합

```
import sys
sys.stdin = open("구간합.txt", "r")

T = int(input())
for tc in range(1,  T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    #print(numbers)
    count = 0
    li = []
    for i in range(len(numbers)-M+1):
         li.append(sum(numbers[i:i+M]))
    print("#%d" % tc, max(li)-min(li))
```



### 1208_Flatten

```python
def index(numbers):
    M = numbers[0]
    M_index = 0
 
    m = numbers[0]
    m_index = 0
    for i, item in enumerate(numbers):
        if M < item:
            M = item
            M_index = i
        if m > item:
            m = item
            m_index = i
    return M_index, m_index
 
 
T = 10
for tc in range(1, T+1) :
    N = int(input())
    numbers = list(map(int, input().split()))
    for n in range(N):
        M_index, m_index = index(numbers)
        numbers[M_index] -= 1
        numbers[m_index] += 1
 
    print("#%d" % tc, max(numbers)-min(numbers))
```



