def largest(arr):
    arr = sorted(arr)
    return arr[-1]

arr = [43,25,63,61,81,13,4]
print(largest(arr))