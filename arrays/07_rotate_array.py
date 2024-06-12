def rotate(arr, k):
    temp = 0
    while k > 0:
        temp = arr[0]
        for j in range(1, len(arr)):
            arr[j-1] = arr[j]
        arr[-1] = temp
        k-=1
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate(arr,2))