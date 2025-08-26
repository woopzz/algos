"""
That XOR Trick
https://florian.github.io//xor-trick/

x y x^y
0 0  0
0 1  1
1 0  1
1 1  0

x ^ 0 = x
x ^ x = 0
x ^ y = y ^ x (commutativity)
"""

def find_missing(arr, n):
    """
    x1 ^ x3 ^ y1 ^ y2 ^ y3 =
    (x1 ^ y1) ^ (x3 ^ y3) ^ y2 =
    0 ^ 0 ^ y2 =
    y2
    """
    result = 0
    for x in range(1, n+1):
        result ^= x

    for x in arr:
        result ^= x

    return result

# Same thing. A duplicate becomes missing, because x^x=0.
find_duplicate = find_missing

def find_two_missing_or_dup(arr, n):
    axorb = find_duplicate(arr, n)
    if not axorb:
        raise Exception('There have to be two different numbers.')

    # "in twos-complement notation i & -i zeroes all but the lowest set bit"
    # https://wiki.python.org/moin/BitManipulation
    mask = axorb & -axorb

    first = 0
    second = 0
    for x in range(1, n+1):
        if x & mask:
            first ^= x
        else:
            second ^= x

    for x in arr:
        if x & mask:
            first ^= x
        else:
            second ^= x

    return first, second

# in-place swaping
a = 1
b = 2
print(f'{a=}, {b=}')
a ^= b  # a = a^b, ----- b = b
b ^= a  # a = a^b, ----- b = b^a^b = a
a ^= b  # a = a^b^a = b, b = a
print(f'{a=}, {b=}')

print('missing =', find_missing([1, 2, 4, 5], 5))
print('duplicate =', find_duplicate([1, 2, 3, 4, 4, 5], 5))
print('two missing =', find_two_missing_or_dup([1, 2, 4], 5))
print('two dupplicates =', find_two_missing_or_dup([1, 1, 2, 2, 3, 4, 5], 5))
