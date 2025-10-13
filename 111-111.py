def binary_search(arr, target):
    if not arr:
        return -1
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        try:
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid+1
            else:
                r = mid-1
        except TypeError:
            return -1
    return -1


arr = [1, 2, 3, 4, 5, 5.5, 10, 7, 8, 9]
print(binary_search(arr, 10))
