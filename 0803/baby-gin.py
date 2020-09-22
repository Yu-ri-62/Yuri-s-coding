num = 456789
c = [0] * 12    # []안에 0이 12개
for i in range(6):
    c[num % 10] += 1  #리스트 c의 num%10의 인덱스에 1추가
    num //= 10        #num //10이 num으로 바뀜

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3 :       # tri 3장의 카드가 동일한 번호
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:   # run 3장의 카드가 연속적인 번호를 갖는 경우
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if tri + run == 2:
    print("Baby Gin")   # run과 triple로만 구성된 경우
else:
    print("Lose")