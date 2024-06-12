def check_if_subset(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in arr1:
        if i not in arr2:
            return False
    return True

arr1 = [1,3,4,5,2]
arr2 = [4,5,2]
if check_if_subset(arr1, arr2):
    print('arr1[] is subset of arr2[]')
else:
    print('arr1[] is not subset of arr2[]')