def rearrange(arr):
    half= len(arr)//2
    arr = sorted(arr)
    first = arr[:half]
    second = arr[half:]
    second = second[::-1]
    for i in second:
        first.append(i)
    return first

arr = [8 ,7, 1, 6, 5, 9]
print(rearrange(arr))