def reverseArray(arr: list) -> list:
    for i in range(len(arr) // 2):
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    return arr
