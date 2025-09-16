def second_largest(arr):
    # Ensure the list has at least 2 distinct elements
    if len(arr) < 2:
        return "List should have at least two elements."

    largest = second = -9999999
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
            
    # If no valid second largest number found (e.g., when all elements are the same)
    if second == -9999999:
        return "There is no second largest number."
    
    return second

# Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

# Output
print("Second largest:", second_largest(arr))