def remove_dup(arr):
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)
    return ans

def opt_remove_dup(arr):
    i = 0
    j = 1
    ans = [arr[0]]
    while j<len(arr):
        if arr[i]!=arr[j]:
            ans.append(arr[j])
            i =j
            j+=1
        j +=1
    return ans

arr = [1,1,1,2,2,3,3,3,3,4,4]
print(opt_remove_dup(arr))