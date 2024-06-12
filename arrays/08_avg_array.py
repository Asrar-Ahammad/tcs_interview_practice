def average_arr(arr):
    sum = 0
    n = len(arr)
    for i in arr:
        sum+=i
    return sum/n

arr = [1, 2, 3, 4, 5]
print(average_arr(arr))