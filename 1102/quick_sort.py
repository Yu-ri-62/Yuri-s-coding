def quick_sort(arr,left,right):
    #시작과 끝점을 기준으로 작업하는데, 시작점이 끝점 보다 작을 때만 실행
    if left < right:
        pivot = lomuto_partition(arr,left,right)
        #피벗을 기준으로 큰값과, 작은값으로 정렬(partition)
        #왼쪽 부분집합 정렬 실행
        quick_sort(arr,left,pivot-1)
        #오른쪽 부분집합 정렬 실행
        quick_sort(arr,pivot+1,right)


def hoare_partition(arr,left,right):
    i = left
    j = right
    pivot = arr[left]

    # i가 j 보다 작거나 같을 때 까지 계속 반복(left와 right가 역전되면 수행 X)
    while i<= j:
        #i는 증가하면서, pivot보다 큰값을 찾음
        while arr[i] <= pivot:
            i += 1
        #j는 감소하면서, pivot보다 작은값을 찾음.
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    #피벗보다 작은값중 제일 뒤에 위치한 arr[j]와 pivot의 위치를 바꿔줌
    arr[j], arr[left] = arr[left], arr[j]
    return j


def lomuto_partition(arr,left,right):
    #오른쪽 피벗으로 설정
    pivot = arr[right]
    i = left -1
    for j in range(left,right):
        # arr[j]이 pivot 보다 작은값을 찾음
        if arr[j] < pivot:
            i += 1  #작다면 i의 인덱스를 옮겨줌,
            # i의 인덱스는 pivot보다 큰 위치에 두어야 함
            arr[i],arr[j] = arr[j], arr[i]
        #i가 가리키는 위치는 pivot보다 작은 값의 마지막인덱스
        #i + 1의 위치에 pivot을 둠
    #수정전 :
        # arr[i + 1], arr[right] = arr[right], arr[i + 1]
        # return i + 1
    #수정 후: 들여쓰기가 잘못되어 있었습니다.
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


arr = [4,3,2,1,7,5,5,2]
quick_sort(arr,0,len(arr)-1)
print(arr)