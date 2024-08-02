"""
Check if array contains a pair of duplicate values, where the two duplicates are no further than k positions from each other(i.e.
arr[i] == arr[j] and abs(i - j) <= k).
O(n * k)
"""

# T: O(n * k) where n is the length of nums
# Note: In the worst case, for each `L`, the inner loop runs k times. It's for the worst case, OFC in avg, the
# inner loop won't run k times every time. For example like when we're close to the end of the arr.

# M: O(1)
def closeDuplicateBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True

    return False
