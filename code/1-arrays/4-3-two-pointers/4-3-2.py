# Q: Given a sorted input array, return the two indices of two elements(so they have to be in different positions)
# which sum up to the target value.
# Assume there's exactly one solution
from typing import List

# The brute-force way is to sum every pair of els to each other. We take every single pair of els, add them together
# and check if they're equal to the target. If they are, we return the indices of those two values.
# T: O(n^2)
# M: O(1)

# The input arr is sorted. So the largest el is at the right most index.

# T: O(n). In worst case, we would look at every single position in the input arr.
# M: O(1)
def targetSum(nums: List[int], target: int) -> [int, int]:
    L, R = 0, len(nums) - 1

    # As the descriptions mentioned, we're guaranteed that there's a solution, so we know this while loop is never gonna
    # never gonna exit without exiting the whole func, so we don't need to put a return after the while. We know we're gonna
    # find a solution in this loop.
    while L < R:
        curr_sum = nums[L] + nums[R]

        if curr_sum < target:
            L += 1
        elif curr_sum > target:
            R -= 1
        else:
            return [L, R]