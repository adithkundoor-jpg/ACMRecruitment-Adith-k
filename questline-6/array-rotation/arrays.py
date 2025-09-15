def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Normalize k
    return nums[-k:] + nums[:-k]  

nums_input = input("Enter elements of the array, separated by spaces: ")
k = int(input("Enter number of steps to rotate (k): "))

nums = list(map(int, nums_input.split()))
# Rotate the array
rotated = rotate_array(nums, k)

# Print result
print("Original array:", nums)
print(f"Array after rotating by {k} steps:", rotated)