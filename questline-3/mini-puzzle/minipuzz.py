def rotate_and_convert(binary_str, k):
    k = k % len(binary_str)
    rotated = binary_str[-k:] + binary_str[:-k]
    decimal_value = int(rotated, 2)
    return decimal_value

binary_str = input('enter binary string')
k = 2
result = rotate_and_convert(binary_str, k)
print('original:', binary_str)
print('rotated:', binary_str[-k:] + binary_str[:-k])
print('decimal value:',result)