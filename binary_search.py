import random

def bsearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        y = arr[m]
        if y == x:
            return m
        if y < x:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    arr = list(range(20))
    arr = [random.randint(1, 51) for _ in range(20)]
    arr.sort()
    print('Array:', arr)

    # Simulate the case where the number we're searching for is not in the array.
    x = random.randint(51, 101) if random.random() < 0.15 else random.choice(arr)

    index = bsearch(arr, x)
    print(f'The element {x} was found at index {index}.')
