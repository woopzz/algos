# Good explanation. But the solution only prints the steps what disk and where to move.
# https://leetcode.com/discuss/post/5272714/tower-of-hanoi-by-satvikmpatil-owd6/

def hanoi(n):
    """Returns the number of steps to solve the puzzle with n disks."""
    if n <= 1:
        return n
    return 1 + 2 * hanoi(n-1)
