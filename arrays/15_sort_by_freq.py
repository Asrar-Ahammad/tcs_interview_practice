def sort_freq(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    count = sorted(count.items(),key=lambda x:x[1])
    count = count[::-1]
    ans = []
    for i in count:
        for j in range(i[1]):
            ans.append(i[0])
    return ans

arr = [1, 2, 3, 2, 4, 3, 1, 2]
print(sort_freq(arr))
