from unittest import defaultTestLoader


def insert_in_beginning(arr, ele):
    arr.append(ele)
    n = len(arr) - 1
    while n > 0:
        arr[n] = arr[n - 1]
        n -= 1
    arr[0] = ele
    return arr


def insert_in_end(arr, element):
    arr.append(element)
    return arr


def insert_at(numbers, element, index):
    first = numbers[:index]
    first.append(element)
    second = numbers[index:]
    for i in second:
        first.append(i)
    return first


arr = [10, 9, 14, 8, 20, 48, 16, 9]

print(insert_in_beginning(arr, 25))
print(insert_in_end(arr, 25))
print(insert_at(arr, 25, 2))
