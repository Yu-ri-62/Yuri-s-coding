# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.


# def backtrack(a):
#     if sum(a) == 10:
#         for i in range(len(a)):

def powerset(k, total):
    if k == n:
        if total == 10:
            for i in range(n):
                if c[i]:
                    print(data[i], end="")
            print()
        return
    else:
        c[k] = False
        powerset(k+1, total)
        c[k] = True
        powerset(k+1, total+data[k])

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

