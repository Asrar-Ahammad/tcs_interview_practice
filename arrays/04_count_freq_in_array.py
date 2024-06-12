from itertools import count


def count_freq(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i]+=1
    
    for i in count:
        print(f"{i} --> {count[i]}")

arr = [10,5,10,15,10,5]
count_freq(arr)