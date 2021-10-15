def selectionSort(arr):
    for i in range(len(arr)):
        minimum = arr[i]
        index = i
        for j in range(i, len(arr)):
            if minimum > arr[j]:
                minimum = arr[j]
                index = j
        minimum = arr[i]
        arr[i] = arr[index]
        arr[index] = minimum


def insertionSort(arr):
    for i in range(len(arr)):
        j = i - 1
        element = arr[i]
        while j >= 0:
            if j == 0 and arr[j] > element:
                arr[j] = element
            if arr[j] > element:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = element
                break
            j -= 1


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        i = gap
        while i < len(arr):
            value = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > value:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = value
            i += 1
        gap = gap // 2


def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    b = []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            b.append(arr[i])
            i += 1
        else:
            b.append(arr[j])
            j += 1
    while i <= mid:
        b.append(arr[i])
        i += 1
    while j <= right:
        b.append(arr[j])
        j += 1
    i = left
    for j in b:
        arr[i] = j
        i += 1


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] > pivot:
            j = j - 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def radixSort(A):
    n = len(A)
    a = max(A)
    m = len(str(a))
    l = []
    bins = [l] * 10
    for i in range(m):
        for j in range(n):
            e = (A[j] // pow(10, i)) % 10
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k += 1


s = [8, 6, 7, 9, 4, 56, 58]
radixSort(s)
print(s)
