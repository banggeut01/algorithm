arr = [69, 10, 30, 2, 16, 8, 31, 22]

def quickSort(lo, hi):
    if lo >= hi: return
    i = lo - 1
    for j in range(lo, hi): # lo ~ hi - 1
        if arr[j] < arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    quickSort(lo, i - 1)
    quickSort(i + 1, hi)

print(arr)
quickSort(0, len(arr) - 1)
print(arr)