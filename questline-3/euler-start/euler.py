# solution.py
# Project Euler Problem 1 and Problem 2

# Problem 1: Sum of multiples of 3 or 5 below 1000
total1 = 0
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        total1 += n
print("Problem 1 Answer:", total1)

# Problem 2: Sum of even Fibonacci numbers below 4,000,000
a, b = 1, 2
total2 = 0
while a < 4000000:
    if a % 2 == 0:
        total2 += a
    a, b = b, a + b
print("Problem 2 Answer:", total2)