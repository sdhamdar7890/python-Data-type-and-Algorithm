def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binarySearch(sorted_arr, x, min_index = 0):
    n = len(sorted_arr)
    mid = n//2
    if x == sorted_arr[mid]:
        return min_index + mid
    elif x > sorted_arr[mid]:
        return binarySearch(sorted_arr[mid+1:], x, min_index + mid+1)
    elif x < sorted_arr[mid]:
        return binarySearch(sorted_arr[:mid], x, min_index)
    return -1


