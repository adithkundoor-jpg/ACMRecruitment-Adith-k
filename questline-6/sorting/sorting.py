def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
# Test array
test_array = [5, 2, 9,1, 5, 6]
print("Original array:", test_array)

insertion_sort(test_array)

print("Sorted array:", test_array)
