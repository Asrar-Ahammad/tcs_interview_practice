"""
Ranks the elements of the given array in ascending order.

Args:
    arr (list): The input array to be ranked.

Returns:
    list: The input array with each element replaced by its rank in the sorted array.
"""
def rank_arr(arr):
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        arr[i] = sorted_arr.index(arr[i])+1
    return arr

arr = [20, 15, 26, 2, 98, 6]
print(rank_arr(arr))
