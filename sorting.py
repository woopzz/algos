"""
There is a Leetcode problem to check these algorithms better.
https://leetcode.com/problems/sort-an-array
"""
from random import randint

def insertion_sort(nums):
    for i in range(1, len(nums)):
        num = nums[i]
        pos = i
        while pos > 0 and num < nums[pos-1]:
            nums[pos] = nums[pos-1]
            pos -= 1
        nums[pos] = num

def mergesort(nums):
    n = len(nums)
    if n <= 1:
        return

    p = n // 2
    lnums = nums[:p]
    rnums = nums[p:]

    mergesort(lnums)
    mergesort(rnums)

    l = r = i = 0
    while l < len(lnums) and r < len(rnums):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l += 1
        else:
            nums[i] = rnums[r]
            r += 1
        i += 1

    while l < len(lnums):
        nums[i] = lnums[l]
        l += 1
        i += 1

    while r < len(rnums):
        nums[i] = rnums[r]
        r += 1
        i += 1

def sort(nums):
    # return insertion_sort(nums)
    return mergesort(nums)

if __name__ == '__main__':
    n = 20
    nums = list(range(n))
    for _ in range(50):
        i = randint(0, n-1)
        j = randint(0, n-1)
        nums[i], nums[j] = nums[j], nums[i]

    print('original =', nums)
    sort(nums)
    print('sorted =', nums)
