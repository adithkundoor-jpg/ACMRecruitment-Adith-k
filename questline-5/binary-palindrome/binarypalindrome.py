n1 = 9
n2 = 10
for n in [n1, n2]:
    b = bin(n)[2:]   # convert to binary
    if b == b[::-1]:
        print(n, "in binary", b, "is a Palindrome")
    else:
        print(n, "in binary", b, "is NOT a Palindrome")

