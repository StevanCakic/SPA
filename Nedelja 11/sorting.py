def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr

def bubble_sort(arr): 
    n = len(arr) 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

# Merge sort
# Quick sort

print(selection_sort([1,5,3,2]))
print(bubble_sort([1,5,3,2]))