def remove_dup_usorted(arr):
    count_dict ={}
    ans = []
    for i in arr:
        if i not in count_dict:
            count_dict[i] = 1
    for i in count_dict:
        ans.append(i)
    return ans

arr = [4, 3, 9, 2, 4, 1, 10, 89, 34]
print(remove_dup_usorted(arr))
