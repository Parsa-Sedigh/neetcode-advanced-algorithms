"""
Check if array contains a pair of duplicate values, where the two duplicates are no further than k positions from eaach other(i.e.
arr[i] == arr[j] and abs(i - j) <= k).
O(n * k)
"""


def closeDuplicateBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True

    return False
