def linear_search(arr, k):
    for i in arr:
        if i == k:
            return arr.index(i)
    return -1

def binary_search(arr, k):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [6, 7, 9, 5, 3, 10]
k = 6
print(linear_search(arr,k))
print(binary_search(arr, k))