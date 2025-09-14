#iterative method
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  
    return reversed_str

# Recursive method 
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

# Test string
original = (input("ENTER WORD TO BE REVERSED"))
print("Original string:", original)
print("Reversed (iterative):", reverse_iterative(original))
print("Reversed (recursive):", reverse_recursive(original))