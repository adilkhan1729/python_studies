def PalinArray(arr ,n):
    for item in arr:
        item_reverse = str(item)[::-1]
        if str(item) != item_reverse:
            return False
    return True

arr = [555]
print(PalinArray(arr, len(arr)))